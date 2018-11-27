from django.shortcuts import render
from .models import Opinion
from .forms import ProductForm
from .opinionETL import opinionRunETL, opinionRunE, opinionRunT, opinionRunL
from .productETL import productRunETL, productRunE, productRunT, productRunL
from django.contrib import messages

#variables for temporary data store. 
#they are used to display results on the screen
extractedOpinionData = ''
transformedOpinionData = []
extractedProductData = ''
transformedProductData = []

def home(request):
    return render(request, 'home.html', {})

#page2 render + onclick runETL
def page2(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            productID = form.cleaned_data['productID']#id from input
            print('ProductID: ', productID)
            try:
                opinionRunETL(productID)
                productRunETL(productID)
                return render(request, 'load.html', {})
            except:
                    print("ProductID invalid")
                    messages.error(request, ('ProductID is not valid. Pleace type it correctly!'))
                    return render(request, 'page2.html', {})
    else:
        return render(request, 'page2.html', {})

#extract page render + onclick runE
def extract(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            productID = form.cleaned_data['productID']
            print('ProductID: ', productID)
            global extractedOpinionData, extractedProductData
            try:
                extractedOpinionData = opinionRunE(productID)
                extractedProductData = productRunE(productID)
                return render(request, 'extract.html', {'extractedOpinionData': extractedOpinionData,'extractedProductData': extractedProductData})
            except:
                    print("ProductID invalid")
                    messages.error(request, ('ProductID is not valid. Pleace type it correctly!'))
                    return render(request, 'page2.html', {})
    else:  
        return render(request, 'page2.html', {})  

#transform page render + onclick runT
def transform(request):
    if request.method == 'POST':
        global transformedOpinionData, transformedProductData
        transformedOpinionData = opinionRunT(extractedOpinionData)
        transformedProductData = productRunT(extractedProductData)
        return render(request, 'transform.html', {'transformedOpinionData': transformedOpinionData, 'transformedProductData': transformedProductData})  
    else: 
        return render(request, 'page2.html', {}) 

#load page render + onclick runL
def load(request):
    if request.method == 'POST':
        opinionRunL(transformedOpinionData)
        productRunL(transformedProductData)
        return render(request, 'load.html', {})  
    else: 
        return render(request, 'page2.html', {})  

#opinions page render
def opinions(request):
    allOpinions = Opinion.objects.all
    return render(request, 'opinions.html', {'allOpinions' : allOpinions})
