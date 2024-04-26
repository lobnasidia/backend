from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.Serializer):
    fullname = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
