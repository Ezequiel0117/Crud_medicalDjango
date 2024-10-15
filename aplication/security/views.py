from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def signup(request):
    if request.method == "GET":
        return render(request, "core/signup.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password1'])
                user.save()
                login(request, user)  # Crear cookie y redireccionarlo
                # Return para una vez que termine ahi una vez que se guarde el usuario
                return redirect('core:home')
            except IntegrityError:
                return render(request, "core/signup.html", {
                    'form': UserCreationForm,
                    "error": 'Username already exists'
                })
        return render(request, "core/signup.html", {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })
        
def signout(request):
    logout(request)
    # Return para redireccionar al home después de cerrar sesión
    return redirect('core:home')


def siging(request):
    if request.method == 'GET':
        return render(request, "core/signin.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],password=request.POST
            ['password'])
        if user is None:
            return render(request, 'core/signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('core:home')

