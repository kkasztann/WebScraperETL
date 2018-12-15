from django.shortcuts import render, redirect
from .models import Opinion
from .models import Product
from .forms import ProductForm
from .opinionETL import opinionRunETL, opinionRunE, opinionRunT, opinionRunL
from .productETL import productRunETL, productRunE, productRunT, productRunL
from django.contrib import messages
from django.http import HttpResponseRedirect

# variables for temporary data store.
# they are used to display results on the screen
extractedOpinionData = ''
transformedOpinionData = []
extractedProductData = ''
transformedProductData = []


def home(request):
    return render(request, 'home.html', {})

# run-etl render + onclick runETL


def runETL(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            productID = form.cleaned_data['productID']  # id from input
            print('ProductID: ', productID)
            try:
                opinionRunETL(productID)
                productRunETL(productID)
                return render(request, 'load.html', {})
            except:
                print("ProductID invalid")
                messages.error(
                    request, ('ProductID is not valid. Pleace type it correctly!'))
                return render(request, 'run-etl.html', {})
    else:
        return render(request, 'run-etl.html', {})

# extract page render + onclick runE


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
                sizeProductParameters = len((extractedProductData)[1][0])
                sizeOpinion = len(extractedOpinionData)
                return render(request, 'extract.html', {'sizeProductParameters': sizeProductParameters, 'sizeOpinion': sizeOpinion, 'extractedOpinionData': extractedOpinionData, 'extractedProductData': extractedProductData})
            except:
                print("ProductID invalid")
                messages.error(
                    request, ('ProductID is not valid. Pleace type it correctly!'))
                return render(request, 'run-etl.html', {})
    else:
        return render(request, 'run-etl.html', {})

# transform page render + onclick runT


def transform(request):
    if request.method == 'POST':
        global transformedOpinionData, transformedProductData
        transformedOpinionData = opinionRunT(extractedOpinionData)
        transformedProductData = productRunT(extractedProductData)
        return render(request, 'transform.html', {'transformedOpinionData': transformedOpinionData, 'transformedProductData': transformedProductData})
    else:
        return render(request, 'run-etl.html', {})

# load page render + onclick runL


def load(request):
    if request.method == 'POST':
        opinionRunL(transformedOpinionData)
        productRunL(transformedProductData)
        return render(request, 'load.html', {})
    else:
        return render(request, 'run-etl.html', {})

# opinions page render


def opinions(request):
    allOpinions = Opinion.objects.all
    return render(request, 'opinions.html', {'allOpinions': allOpinions})

# opinions page render


def products(request):
    allProducts = Product.objects.all
    return render(request, 'products.html', {'allProducts': allProducts})


def deleteProduct(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('products')


def deleteProducts(request):
    allProducts = Product.objects.all()
    allProducts.delete()
    return redirect('products')
