from django.forms import ModelForm
from django import forms
from .models import Reminder


class ReminderForm(ModelForm):
    class Meta:
        model = Reminder
        fields = '__all__'

        options ={
            'message':"message",
            'mobile' : 'mobile',
            "email"  : 'email',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'reminder_method': forms.Select(attrs={'class': 'form-control'},choices=options),


        }
