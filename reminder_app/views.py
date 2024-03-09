from django.shortcuts import render
from .forms import ReminderForm

# Create your views here.


def Remind_Later(request):
    form = ReminderForm()
    if request.method == "POST":

        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReminderForm()
    
    context = {
        'form': form
    }
    return render(request, 'api.html', context)
