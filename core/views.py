import uuid
from http.client import HTTPResponse

from django.shortcuts import render, redirect

import core.models
from core.models import Events
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages


@login_required(login_url="/auth/login/")
def lista_eventos(request):
    evento = Events.objects.all()
    if request.user is not None:
        return render(request, "agenda.html", context={"eventos": evento})
    else:
        return redirect("/auth/login/")


def login_user(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_login = authenticate(username=username, password=password)
        if user_login is not None:
            login(request, user_login)
            return redirect("/agenda/")
        else:
            messages.error(request, "Username our password incorrect!")

    return render(request, "auth/login.html")


def logout_user(request):
    logout(request)
    return redirect("/auth/login/")


def submit_login(request):
    if request.POST:
        username = request.POST.get("email")
        password = request.POST.get("password")
        user_login = authenticate(username=username, password=password)
        if user_login is not None:
            login(request, user_login)
            return redirect("/agenda/")
        else:
            messages.error(
                request,
                "Falha na tentativa de autenticação, por favor, vericiar usuário e ou senha!",
            )
    return redirect("/")


def signut_user(request):
    return render(request, "auth/signup.html")


def create_user(request):
    if request.POST:
        if request.POST:
            email = request.POST.get("email")
            password = request.POST.get("password")
            password_confirm = request.POST.get("password_confirm")
            if email and password == password_confirm:
                password = make_password(password)
                user = core.models.User(email=email, password=password)
                user.save()
                return redirect("/")
            else:
                return messages.error(request, "Ocorreu um erro no cadastro!")
    return redirect("/")


def update_or_create_event(request):
    if request.POST:
        event = Events.objects.get(id=id_event)
        user = request.user
        if event:
            if user == event.user:
                event.update()
            else:
                return redirect("/fail/")
        else:
            event.save()

    return render(request, "evento.html")


def fail(request):
    return render(request, "auth/fail.html")
