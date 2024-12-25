import cv2
import numpy as np
from django.http import JsonResponse
import base64
import json
from django.conf import settings


def process_binarization(request):
    if request.method == 'POST':
        try:
            # Парсим JSON данные из запроса
            body = json.loads(request.body)
            image_data = body.get('image')
            threshold = int(body.get('threshold', 127))
            block_size = int(body.get('block_size', 11))
            constant = int(body.get('constant', 10))

            if not image_data:
                return JsonResponse({'error': 'No image data provided'}, status=400)

            # Декодируем изображение из Base64
            header, encoded = image_data.split(',', 1)
            img_data = base64.b64decode(encoded)
            np_img = np.frombuffer(img_data, np.uint8)
            img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

            if img is None:
                return JsonResponse({'error': 'Failed to decode image'}, status=400)

            # Преобразуем в оттенки серого
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Применяем бинаризацию
            if block_size > 3:
                binarized_img = cv2.adaptiveThreshold(
                    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
            else:
                _, binarized_img = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

            # Кодируем результат обратно в Base64
            _, buffer = cv2.imencode('.jpg', binarized_img)
            result_image = base64.b64encode(buffer).decode('utf-8')

            # Возвращаем результат
            return JsonResponse({'image': result_image})
        except Exception as e:
            return JsonResponse({'error': f'Internal server error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
