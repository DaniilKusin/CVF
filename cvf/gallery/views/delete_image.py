from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import UserImage  # Импортируем модель UserImage
from django.contrib import messages


@login_required
def delete_image(request, image_id):
    try:
        image = UserImage.objects.get(id=image_id, user=request.user)
        image.delete()
        messages.success(request, 'Изображение удалено.')
    except UserImage.DoesNotExist:
        messages.error(request, 'Изображение не найдено.')
    return redirect('gallery')
