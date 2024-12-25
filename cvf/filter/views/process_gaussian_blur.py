import cv2
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from io import BytesIO
from PIL import Image
import json


@csrf_exempt
def process_gaussian_blur(request):
    if request.method == 'POST':
        try:
            # Получаем данные из запроса
            data = json.loads(request.body)
            image_data = data.get('image')
            kernel_size = int(data.get('kernel_size', 5))  # Размер ядра
            sigma = float(data.get('sigma', 1))  # Стандартное отклонение (для размытия)

            # Декодируем изображение из base64
            image_data = image_data.split(',')[1]  # Убираем часть "data:image/jpeg;base64,"
            image_data = base64.b64decode(image_data)  # Декодируем base64 в байты
            np_img = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

            if img is None:
                return JsonResponse({'error': 'Failed to decode image'}, status=400)

            # Применяем гауссово размытие с помощью OpenCV
            blurred_image = cv2.GaussianBlur(img, (kernel_size * 2 + 1, kernel_size * 2 + 1), sigma)

            _, buffer = cv2.imencode('.jpg', blurred_image)
            result_image = base64.b64encode(buffer).decode('utf-8')

            # Возвращаем результат
            return JsonResponse({'image': result_image})
        except Exception as e:
            return JsonResponse({'error': f'Internal server error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
