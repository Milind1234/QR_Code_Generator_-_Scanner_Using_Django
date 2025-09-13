import io
import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.base import ContentFile
from django.urls import reverse
from .models import GeneratedQR

# QR generation packages
import qrcode
from PIL import Image

# QR scanning packages
from pyzbar.pyzbar import decode
from PIL import Image as PILImage

def generate_qr(request):
    """
    GET: shows form
    POST: creates QR image, saves model (optional) and displays result
    """
    qr_url = None
    saved_obj = None

    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if text:
            # create qrcode
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            # Save image to in-memory file
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            # Save to model (optional)
            filename = f"qr_{abs(hash(text)) % (10**8)}.png"
            dj_file = ContentFile(buffer.read(), name=filename)

            saved_obj = GeneratedQR.objects.create(text=text, image=dj_file)
            qr_url = saved_obj.image.url

            # Redirect to GET with result or just render
            return render(request, "scanner/generator.html", {"qr_url": qr_url, "text": text, "saved": saved_obj})

    return render(request, "scanner/generator.html", {})


def scan_qr(request):
    """
    GET: upload form
    POST: accept uploaded image and decode qrcode inside
    """
    decoded_text = None
    error = None

    if request.method == "POST":
        uploaded = request.FILES.get('image')
        if not uploaded:
            error = "Please upload an image containing a QR code."
        else:
            try:
                # load image via PIL
                pil_img = PILImage.open(uploaded).convert('RGB')
                # decode using pyzbar
                results = decode(pil_img)
                if results:
                    # For simplicity, take first decoded object
                    decoded_text = results[0].data.decode('utf-8')
                else:
                    error = "No QR code found in the image. Try a clearer picture or crop tightly."
            except Exception as e:
                error = f"Error decoding image: {e}"

    return render(request, "scanner/scan.html", {"decoded_text": decoded_text, "error": error})
