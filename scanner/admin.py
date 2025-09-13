from django.contrib import admin
from .models import GeneratedQR

@admin.register(GeneratedQR)
class GeneratedQRAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created_at")
    readonly_fields = ("created_at",)
