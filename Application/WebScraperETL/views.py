from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def page2(request):
    return render(request, 'page2.html', {})
