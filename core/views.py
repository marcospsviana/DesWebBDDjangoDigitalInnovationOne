from http.client import HTTPResponse

from django.shortcuts import render, redirect
from .models import Events
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Events.objects.all()
    return render(request, 'agenda.html', context={"eventos": evento})



def login_user(request):
    return render(request, 'auth/login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HTTPResponse('usuario nao existe')
    else:
        return redirect('/')
    return render(request, 'auth/submit.html')

def signut_user(request):
    return render(request, 'auth/signup.html')
