
from functools import partial
from unicodedata import category, name
from venv import create
from django.shortcuts import render
from .models import Order, Product
from .serializers import CreateOrderSerializer, ListOrderSerializer, ListProductSerializer, CreateProductSerializer
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
# Create your views here.


class OrderView(ListAPIView):
    '''
    This Class Show all the Order
    '''
    queryset = Order.objects.all()
    serializer_class = ListOrderSerializer
    

class ListProductView(ListAPIView):
    '''
    This Class Show all the Product
    '''
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    

class CreateProductView(APIView):
   
    def post(self, request):
        '''
        This Function get data through POST request and
        build some functionality to calculate price and
        quntity of product and create product record and
        update order record.
        '''
        try:    
            data = request.data

            #Update Order
            p_order = data.get('order')
            p_name = data.get('name')
            p_qty = int(data.get('qty'))
            p_price = int(data.get('price'))
            p_price = p_price * p_qty
            
            
            order_data, created = Order.objects.get_or_create(id = p_order, defaults=None)
            
            order_data.placed =True
            ttl_price = order_data.total_price + p_price
            ttl_qty = order_data.total_qty + p_qty   
            order_dict = {
                'placed':True,
                'total_price': ttl_price,
                'total_qty': ttl_qty,
            }
 
            product_serializer = CreateProductSerializer(data=data)
            order_serializer = CreateOrderSerializer(instance=order_data, data=order_dict, partial=True)
            if product_serializer.is_valid() and order_serializer.is_valid():
                product_serializer.save()
                order_serializer.save()
                    
                res = {
                    'msg': 'Product created..',
                    'msg1': 'Order Updated..'
                }
                return Response(res)
            else:
                res = {'msg': 'Product not created..'}

        except:
            res = {'msg': 'Product not created..'}      
        return Response(res)



# temporary json data
# {
# "order" : "1",
# "category" : "Electronics",
# "brand" : "LG",
# "name" : "MACHINE",
# "price" : "20000",
# "qty" : "1"
# }

        
        
        

       
        

        

