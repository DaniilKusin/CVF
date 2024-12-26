from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from ..models import UserImage


def download_image(request, image_id):
    user_image = get_object_or_404(UserImage, id=image_id, user=request.user)
    try:
        return FileResponse(user_image.image.open(), as_attachment=True, filename=user_image.filename())
    except FileNotFoundError:
        raise Http404("File not found")
