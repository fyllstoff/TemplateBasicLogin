from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegistroForm
from django.contrib import messages




def bienvenido(request):
    return render(request, 'bienvenido.html')

login_attempts = {}

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. ¡Ahora puedes iniciar sesión!")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    global login_attempts
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # Control de intentos
        if username in login_attempts and login_attempts[username] >= 3:
            messages.error(request, "Clave bloqueada. Contacte al administrador.")
            return render(request, 'login.html')

        if user is not None:
            login(request, user)
            login_attempts.pop(username, None)  
            return redirect('bienvenido')  
        else:
            login_attempts[username] = login_attempts.get(username, 0) + 1
            messages.error(request, "Credenciales inválidas.")
    return render(request, 'login.html')


 

def index(request):
    return redirect('login')


