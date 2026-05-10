from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insects.urls')),  # Include URLs from the insects app
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'insects.views.error_404'
handler500 = 'insects.views.error_500'