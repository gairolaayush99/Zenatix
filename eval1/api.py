from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.utils import timezone
import datetime

@api_view(["POST"])
def AddIngredients(request):
    serializer=IngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return  Response(serializer.errors,status=400)
        
    return Response(serializer.data,status=201)

@api_view(["GET"])
def Ingredient(request):
    ingredient=Ingredients.objects.all()
    serializer=IngredientSerializer(ingredient,many=True)
    return Response(serializer.data,status=200)



@api_view(["GET"])
def history(request):
    histry=History.objects.all()
    serializer=HistorySerializer(histry,many=True)
    return Response(serializer.data,status=200)

@api_view(["POST"])
def Supply(request):
    serializer=SupplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return  Response(serializer.errors,status=400)
    return Response(serializer.data,status=201)

@api_view(["GET"])
def product(request):
    prdcts=Products.objects.all()
    serializer=SupplySerializer(prdcts,many=True)
    return Response(serializer.data,status=200)

@api_view(["POST"])
def inventory(request):
    serializer=HistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return  Response(serializer.errors,status=400)
    return Response(serializer.data,status=201)
