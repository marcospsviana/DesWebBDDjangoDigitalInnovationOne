from django.urls import path
from . import views


urlpatterns = [
    path('agenda/', views.lista_eventos),
    path('login/', views.login_user),
    path('login/submit/', views.submit_login),
    path('login/signup/', views.signut_user)
]