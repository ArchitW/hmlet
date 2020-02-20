from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from ..models import Photo
from .serializers import PhotoSerializer


class PhotoListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Photo.objects.all()
        serializer = PhotoSerializer(qs, many=True)
        return Response(serializer.data)


class PhotoAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):

    permission_classes = []
    authentication_classes = []
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        qs = Photo.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
