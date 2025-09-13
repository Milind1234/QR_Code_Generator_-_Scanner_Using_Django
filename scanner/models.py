from django.db import models

class GeneratedQR(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='qrcodes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR {self.id} - {self.text[:20]}"
