from django.db import models


def user_directory_path(instance, filename):
    """
    Генерирует путь для загрузки файлов, используя имя пользователя.
    Путь будет вида: 'user_images/<username>/<filename>'
    """
    return f'user_images/{instance.user.username}/{filename}'


class UserImage(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image by {self.user.username} ({self.uploaded_at})"

    def filename(self):
        return self.image.name.split('/')[-1]  # Возвращает имя файла
