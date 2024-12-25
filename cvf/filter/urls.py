from django.urls import path
from .views import binarization_page, process_binarization, gaussian_blur, process_gaussian_blur, canny, process_canny

urlpatterns = [
    path('binarization/', binarization_page, name='binarization'),
    path('binarization/process_binarization/', process_binarization, name='process_binarization'),
    path('gaussian_blur/', gaussian_blur, name='gaussian_blur'),
    path('gaussian_blur/process_gaussian_blur/', process_gaussian_blur, name='process_gaussian_blur'),
    path('canny/', canny, name='canny'),
    path('canny/process_canny/', process_canny, name='process_canny'),
]
