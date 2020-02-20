import json

from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from ..models import Photo
from .serializers import PhotoSerializer


def is_json(json_data):
    '''verifies given data is json or not'''
    try:
        is_json_data = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


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
    passed_id =  None

    def get_queryset(self):
        qs = Photo.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def perform_destroy(self,instance):
        if instance is not None:
            return instance.delete()
        return None

    def get(self, request, *args, **kwargs):
        #print(request.body)
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        if is_json(request.body):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id

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
