from django.urls import path
from . import views


urlpatterns = [
    # path('agenda/', views.lista_eventos),
    path("login/", views.login_user),
    path("submit/", views.submit_login),
    path("signup/", views.signut_user),
    path("register/", views.create_user),
    path("fail/", views.fail),
    path("logout/", views.logout_user),
    path("event/", views.update_or_create_event),
]
