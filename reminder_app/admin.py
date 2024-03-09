from django.contrib import admin
from .models import Reminder
# Register your models here.
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['date','time', 'message', 'reminder_method']

admin.site.register(Reminder,ReminderAdmin)