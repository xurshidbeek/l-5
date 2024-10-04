from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_main.urls')),
    path('users/', include('app_users.urls'))
    
] + static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
