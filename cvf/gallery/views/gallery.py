from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import UserImage  # Импортируем модель UserImage
from django.contrib import messages


@login_required
def gallery(request):
    images = UserImage.objects.filter(user=request.user)
    return render(request, 'gallery/gallery.html', {'images': images})
