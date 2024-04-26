from rest_framework import serializers

from .models import Blog, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = "__all__"
