from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('upload_photo', permanent=False)),  # Redirect root to upload
    path('photo_filter/', include('photo_filter.urls')),  # Make sure the path here matches the app name
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
