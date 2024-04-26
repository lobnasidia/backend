from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = cache.get("feedbacks")
        if queryset is None:
            queryset = Feedback.objects.all()
            cache.set("feedbacks", queryset, 60)
        serializer = FeedbackSerializer(queryset, many=True)
        return Response(serializer.data)
