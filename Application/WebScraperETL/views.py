from django.shortcuts import render
from .models import Opinion

def home(request):
    return render(request, 'home.html', {})

def page2(request):
    return render(request, 'page2.html', {})

def opinions(request):
    allOpinions = Opinion.objects.all
    return render(request, 'opinions.html', {'allOpinions' : allOpinions})
