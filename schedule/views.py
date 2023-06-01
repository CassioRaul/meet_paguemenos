from django.shortcuts import render
from .models import Schedule

def schedule(request):
    schedule = Schedule.objects.all()

    context={
       'schedule':schedule
    }
    return render(request, 'schedule/index.html', context)


