from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('page2/', views.page2, name='run-etl'),
    path('page2/extract', views.extract, name='run-e'),
    path('page2/transform', views.transform, name='run-t'),
    path('page2/load', views.load, name='run-l'),
    path('opinions/', views.opinions, name='opinions'),
]
