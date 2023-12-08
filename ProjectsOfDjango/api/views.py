from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from loginapp.models import OmsAdmin
from .serializers import OrderSerializer
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def get_orders(request,id='',format=''):
    if request.method == 'GET' and id=='':
        order = OmsAdmin.objects.all()
        serializer = OrderSerializer(order,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method =='GET' and id!='':
        try:
            order = OmsAdmin.objects.all().get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    elif request.method == 'PUT':
        try:
            order = OmsAdmin.objects.all().get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
    elif request.method == 'DELETE':
        try:
            order = OmsAdmin.objects.all().get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
