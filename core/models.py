from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    event_day = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title

    def get_event_date(self):
        return f'{self.event_day: %d - %m - %Y }'
