from django.urls import path
from .views import gallery, delete_image, save_image_from_canvas


urlpatterns = [
    path('', gallery, name='gallery'),
    path('delete_image/<int:image_id>/', delete_image, name='delete_image'),
    path('save/', save_image_from_canvas, name='save_image'),

]
