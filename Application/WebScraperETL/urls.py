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
]
