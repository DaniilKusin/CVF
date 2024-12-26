from django.http import JsonResponse
from django.core.files.base import ContentFile
import base64
from ..models import UserImage
from django.contrib.auth.decorators import login_required
import json


@login_required
def save_image_from_canvas(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            image_data = data.get('image')
            description = data.get('description', '')

            # Декодирование изображения из Base64
            format, imgstr = image_data.split(';base64,')  # Убираем метаданные
            ext = format.split('/')[-1]  # Определяем расширение
            file_data = ContentFile(base64.b64decode(imgstr), name=f"image.{ext}")

            # Сохранение изображения
            UserImage.objects.create(user=request.user, image=file_data, description=description)
            return JsonResponse({'message': 'Изображение успешно сохранено!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Неверный метод'}, status=405)
