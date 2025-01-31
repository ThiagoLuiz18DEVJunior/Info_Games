from django.shortcuts import *
from .views import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_info_games (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/listar/?model=games')
        else:
            messages.error(request, 'Usuário ou Senha Incorretos.')
            return render(request, 'login.html')
    else:
	    return render(request, 'login.html')


@login_required
def logout_info_games (request):
        logout(request)
        return redirect('login')

# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.models import User

# Função de registro de usuário
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()  
            messages.success(request, "Conta criada com sucesso! Você pode agora fazer login.")
            return redirect('login') 
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    user = request.user 
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)  
        if form.is_valid():
            form.save() 
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('profile')  
    else:
        form = UserForm(instance=user)  

    return render(request, 'profile.html', {'form': form, 'user': user})