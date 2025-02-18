# urls.py

from django.urls import path
from . import views

app_name="login"

urlpatterns = [
    path('', views.home_view, name='home'),  # Página de inicio
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard
]