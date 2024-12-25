from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import main_page, user_profile, register, filters_page, info


urlpatterns = [
    path('main_page/', main_page, name='main_page'),
    path('', main_page, name='main_page'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', user_profile, name='user_profile'),
    path('filter/', filters_page, name='filter'),
    path('info/', info, name='info'),
]
