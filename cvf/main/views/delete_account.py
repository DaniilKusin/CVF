from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        username = user.username
        user.delete()  # Удаляем текущего пользователя
        messages.success(request, f'Аккаунт {username} был успешно удален.')
        return redirect('')  # Перенаправляем на главную страницу
    return redirect('user_profile')  # Перенаправляем на профиль, если запрос не POST
