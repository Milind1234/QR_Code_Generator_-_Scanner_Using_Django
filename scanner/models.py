# scanner/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class GeneratedQR(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='generated_qrs')
    text = models.TextField()
    image = models.ImageField(upload_to='qrcodes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR {self.id} - {self.text[:20]}"
