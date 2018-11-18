from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page2/', views.page2, name='run-etl'),
    path('page2/', views.page2, name='products'),
]
