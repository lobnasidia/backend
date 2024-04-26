from rest_framework import serializers

from .models import Category, Service, ServiceIndex


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Service
        fields = "__all__"


class ServiceIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceIndex
        fields = "__all__"
