from django.shortcuts import render
from .models import Opinion
from .forms import ProductForm
from .ETL import runETL, runE, runT, runL

extractedData = ''
transformedData = []

def home(request):
    return render(request, 'home.html', {})

def page2(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            productID = form.cleaned_data['productID']
            print('ProductID: ', productID)
            runETL(productID)
            return render(request, 'load.html', {})
    else:
        #should redirect to invalid data html 
        return render(request, 'page2.html', {})

def extract(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            productID = form.cleaned_data['productID']
            print('ProductID: ', productID)
            global extractedData
            extractedData = runE(productID)
            return render(request, 'extract.html', {'extractedData' : extractedData})
    else:
        #should redirect to invalid data html    
        return render(request, 'page2.html', {})  

def transform(request):
    if request.method == 'POST':
        #if not null   
        global transformedData 
        transformedData = runT(extractedData)
        return render(request, 'transform.html', {'transformedData' : transformedData})  
    else:
        #should redirect to invalid data html    
        return render(request, 'page2.html', {}) 

def load(request):
    if request.method == 'POST':
        #if not null   
        runL(transformedData)
        return render(request, 'load.html', {})  
    else:
        #should redirect to invalid data html    
        return render(request, 'page2.html', {})  

def opinions(request):
    allOpinions = Opinion.objects.all
    return render(request, 'opinions.html', {'allOpinions' : allOpinions})
