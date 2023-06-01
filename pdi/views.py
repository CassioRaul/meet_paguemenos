from django.shortcuts import render
from .models import Planning


def pdi(request):
    planning = Planning.objects.all()
    
    context={
        'planning':planning
    }
    
    return render(request, 'pdi/index.html', context)
