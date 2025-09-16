# core/views.py
import logging

from django.shortcuts import render
from django.apps import apps
from django.views.decorators.cache import cache_page

logger = logging.getLogger(__name__)

# Cache the rendered homepage for 60 seconds (adjust as needed)
@cache_page(60)
def home(request):
    """
    Home view — shows a short welcome and, if the 'scanner' app is installed,
    shows a few recent generated QR objects (if the model exists).

    Improvements:
    - logs exceptions instead of silently swallowing them
    - uses .only(...) to fetch only needed fields
    - caches the homepage for 60 seconds
    - tries to show per-user qrs if GeneratedQR has a user FK
    """
    recent = []

    if apps.is_installed('scanner'):
        try:
            GeneratedQR = apps.get_model('scanner', 'GeneratedQR')

            # Build a base queryset ordered newest first
            qs = GeneratedQR.objects.order_by('-created_at')

            # Micro-optimization: fetch only the fields used in template
            # (text, image, created_at). If your model uses different names, adjust.
            qs = qs.only('text', 'image', 'created_at')

            # If the model has a 'user' field and the request user is authenticated,
            # show per-user recent items. This is defensive: it checks for field existence.
            if request.user.is_authenticated:
                try:
                    # Use _meta to check for field existence without causing import errors
                    GeneratedQR._meta.get_field('user')
                    qs = qs.filter(user=request.user)
                except Exception:
                    # model has no 'user' field — show global recent
                    pass

            recent = list(qs[:6])  # evaluate queryset here

        except Exception as e:
            # Log the full stacktrace to help debugging while keeping the site up.
            logger.exception("Failed to load GeneratedQR for homepage: %s", e)
            recent = []

    return render(request, 'core/home.html', {"recent": recent})
