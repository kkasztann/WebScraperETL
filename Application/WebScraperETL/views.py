from django.shortcuts import render
from .models import Opinion
from .forms import ProductForm
from .ETL import runETL

def home(request):
    return render(request, 'home.html', {})

def page2(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            print('ProductID', form.cleaned_data['productID'])
            runETL(form.cleaned_data['productID'])
            form.save()
            return render(request, 'page2.html', {})
    else:
        return render(request, 'page2.html', {})
        
def opinions(request):
    allOpinions = Opinion.objects.all
    return render(request, 'opinions.html', {'allOpinions' : allOpinions})
