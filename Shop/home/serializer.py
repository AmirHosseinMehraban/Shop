from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(ProductSerializer, self).to_representation(instance)
        rep['category'] = instance.category.name
        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
