from django.contrib import admin
from .models import ClickCounter

@admin.register(ClickCounter)
class ClickCounterAdmin(admin.ModelAdmin):
    list_display = ['id', 'clicks', 'reset_count', 'level']

# Register your models here.
