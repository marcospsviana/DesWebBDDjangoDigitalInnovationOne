from django.contrib import admin
from .models import Events

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    model = Events
    fields = ['title', 'description', 'event_day']
