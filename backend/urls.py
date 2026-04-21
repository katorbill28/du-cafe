from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Import this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() # Add this line
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
