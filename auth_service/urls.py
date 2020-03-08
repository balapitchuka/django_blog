from django.urls import path
from django.contrib.auth import views as auth_views
from auth_service import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth_service/login.html'), name='auth-login'),
    path('register/', views.register, name='auth-register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth_service/logout.html'), name='auth-logout'),
]
