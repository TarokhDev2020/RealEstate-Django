from os import stat
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("pages.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URI, document_root=settings.MEDIA_ROOT)
