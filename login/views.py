from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def home_view(request):
    # Si el usuario ya está autenticado, redirigirlo al dashboard
    if request.user.is_authenticated:
        return redirect('login:dashboard')
    
    # Si no está autenticado, mostrar la página de inicio
    return render(request, 'home.html')  # Plantilla en templates/home.html

@login_required  # Asegura que solo los usuarios autenticados puedan acceder
def dashboard_view(request):
    return render(request, 'dashboard.html')  # Renderiza la plantilla dashboard.html

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login:dashboard')  # Redirigir al dashboard después del registro
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})

def login_view(request):
    # Si el usuario ya está autenticado, redirigirlo al dashboard
    if request.user.is_authenticated:
        return redirect('login:dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login:dashboard')  # Redirigir al dashboard después del login
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login:home')  # Redirige a la vista 'home'