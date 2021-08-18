from django.contrib import admin
from .models import Events, User


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    model = Events
    fields = ["title", "description", "event_day"]


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    model = User
    fields = ["email", "first_name", "is_staff", "date_joined", "password"]
