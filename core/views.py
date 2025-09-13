from django.shortcuts import render
from django.apps import apps

def home(request):
    """
    Home view — shows a short welcome and, if the 'scanner' app is installed,
    shows a few recent generated QR objects (if the model exists).
    """
    recent = []
    # Use the apps registry API to check if the app is installed
    if apps.is_installed('scanner'):
        try:
            # Import the model dynamically to avoid import-time errors if app missing
            GeneratedQR = apps.get_model('scanner', 'GeneratedQR')
            recent = GeneratedQR.objects.order_by('-created_at')[:6]
        except Exception:
            # If anything goes wrong (model not present yet), keep recent = []
            recent = []

    return render(request, 'core/home.html', {"recent": recent})
