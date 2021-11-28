from rest_framework import serializers
from .models import Ingredients,History,Products

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredients
        fields="__all__"

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=History
        fields="__all__"
class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"

