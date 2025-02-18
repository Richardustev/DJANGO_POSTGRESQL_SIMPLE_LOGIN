from django.contrib import admin
from django.urls import path, include
from login.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),  # Incluye las URLs de la aplicación "login"
]