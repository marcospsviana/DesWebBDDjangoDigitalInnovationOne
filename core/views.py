from http.client import HTTPResponse

from django.shortcuts import render, redirect
from core.models import Events
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest
from django.contrib import messages


@login_required(login_url='/auth/login/')
def lista_eventos(request):
    evento = Events.objects.all()
    if request.user is not None:
        return render(request, 'agenda.html', context={"eventos": evento})
    else:
        return redirect('/auth/login/')

    # return render(request, 'agenda.html', context={"eventos": evento})


def login_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_login = authenticate(username=username, password=password)
        if user_login is not None:
            login(request, user_login)
            return redirect('/agenda/')
        else:
            messages.error(request, "Username our password incorrect!")

    return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    return redirect('/auth/login/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('email')
        password = request.POST.get('password')
        user_login = authenticate(username=username, password=password)
        if user_login is not None:
            login(request, user_login)
            return redirect('/agenda/')
        else:
            messages.error(request, "Falha na tentativa de autenticação, por favor, vericiar usuário e ou senha!")
    return redirect('/')


def signut_user(request):
    return render(request, 'auth/signup.html')


def fail(request):
    return render(request, 'auth/fail.html')