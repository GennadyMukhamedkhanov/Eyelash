from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from my_site.views import RegistrationView
from conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_site.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)