from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from django.utils import timezone
from .permissions import *
import datetime

@api_view(["POST"])
@permission_classes([ProducrPermission,])
def AddIngredients(request):
    serializer=IngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return  Response(serializer.errors,status=400)
        
    return Response(serializer.data,status=201)

@api_view(["GET"])
@permission_classes([ConsumerPermission,])
def Ingredient(request):
    ingredient=Ingredients.objects.all()
    serializer=IngredientSerializer(ingredient,many=True)
    return Response(serializer.data,status=200)



@api_view(["GET"])
@permission_classes([ConsumerPermission,])
def history(request):
    page = int(request.GET.get('page', '1'))
    size = 10
    histry=History.objects.all()[size*(page-1):size*page]
    serializer=HistorySerializer(histry,many=True)
    return Response(serializer.data,status=200)

@api_view(["POST"])
@permission_classes([ConsumerPermission,])
def Supply(request):
    serializer=SupplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return  Response(serializer.errors,status=400)
    return Response(serializer.data,status=201)

@api_view(["GET"])
@permission_classes([ConsumerPermission,])
def product(request):
    prdcts=Products.objects.all()
    serializer=SupplySerializer(prdcts,many=True)
    return Response(serializer.data,status=200)

@api_view(["POST"])
@permission_classes([ProducrPermission,])
def inventory(request):
    serializer=HistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return  Response(serializer.errors,status=400)
    return Response(serializer.data,status=201)
