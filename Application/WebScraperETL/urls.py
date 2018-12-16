from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('run-etl/', views.runETL, name='run-etl'),
    path('run-etl/extract', views.extract, name='run-e'),
    path('run-etl/transform', views.transform, name='run-t'),
    path('run-etl/load', views.load, name='run-l'),
    path('opinions/', views.opinions, name='opinions'),
    path('products/', views.products, name='products'),
    path('delete/<product_id>', views.deleteProduct, name='delete-product'),
    path('delete-products', views.deleteProducts, name='delete-products'),
    path('products/orderAsc', views.sortNameAscending, name='sort-name-ascending'),
    path('products/orderDesc', views.sortNameDescending, name='sort-name-descending'),
    path('details-product/<product_id>', views.productDetails, name='details-product'),
    path('csv/<product_id>', views.productCSV, name='csv-product'),
    path('csv-products>', views.productsCSV, name='csv-products'),
]
