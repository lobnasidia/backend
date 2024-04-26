from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Service, ServiceIndex
from .serializers import ServiceIndexSerializer, ServiceSerializer


class ServiceViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        index_param = request.query_params.get("index", None)
        if index_param is not None and index_param.lower() == "true":
            queryset = Service.objects.filter(index=True)
            cache_key = "service_index_true"
        elif index_param is not None and index_param.lower() == "false":
            queryset = Service.objects.filter(index=False)
            cache_key = "service_index_false"
        else:
            queryset = cache.get("service_index_all")
            if queryset is None:
                queryset = Service.objects.all()
                cache.set("service_index_all", queryset, 60)
            cache_key = "service_index_all"
        serializer = ServiceSerializer(queryset, many=True)
        cache.set(cache_key, queryset, 60)
        return Response(serializer.data)


class ServiceIndexViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = cache.get("services-index")
        if queryset is None:
            queryset = ServiceIndex.objects.all()[:1]
            cache.set("services-index", queryset, 60)
        serializer = ServiceIndexSerializer(queryset, many=True)
        return Response(serializer.data)
