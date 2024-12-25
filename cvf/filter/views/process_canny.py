import cv2
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import json


@csrf_exempt
def process_canny(request):
    if request.method == 'POST':
        try:
            # Получаем данные из запроса
            data = json.loads(request.body)
            image_data = data.get('image')
            low_threshold = int(data.get('low_threshold', 50))  # Нижний порог
            high_threshold = int(data.get('high_threshold', 150))  # Верхний порог

            # Декодируем изображение из base64
            image_data = image_data.split(',')[1]  # Убираем часть "data:image/jpeg;base64,"
            image_data = base64.b64decode(image_data)  # Декодируем base64 в байты
            np_img = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

            # Преобразуем изображение в оттенки серого (необходим для детектора Кэнни)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Применяем детектор границ Кэнни
            edges = cv2.Canny(gray_image, low_threshold, high_threshold)

            _, buffer = cv2.imencode('.jpg', edges)
            result_image = base64.b64encode(buffer).decode('utf-8')

            # Возвращаем результат
            return JsonResponse({'image': result_image})
        except Exception as e:
            return JsonResponse({'error': f'Internal server error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
