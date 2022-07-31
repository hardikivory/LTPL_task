

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.OrderView.as_view(), name='order'),
    path('product/', views.ListProductView.as_view(), name='product'),
    path('create_product/', views.CreateProductView.as_view(), name='create_product'),
    
]