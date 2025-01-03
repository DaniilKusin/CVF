from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filter/', include('filter.urls')),
    path('gallery/', include('gallery.urls')),
    path('main/', include('main.urls')),
    path('', RedirectView.as_view(url='/main/', permanent=True)),
]
# Обработка медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
