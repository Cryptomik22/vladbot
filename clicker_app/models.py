# clicker_app/models.py
from django.db import models

class ClickCounter(models.Model):
    clicks = models.IntegerField(default=0)
    reset_count = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    class Meta:
        app_label = 'clicker_app'  # Явное указание app_label

    def __str__(self):
        return f'Clicks: {self.clicks}'
