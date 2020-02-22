import json

from rest_framework.authentication import SessionAuthentication
from rest_framework import generics, mixins, permissions, pagination
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from accounts.api.permissions import IsOwnerOrReadOnly

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


class PageNumbers(pagination.PageNumberPagination):
    page_size = 10


class PhotoAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PageNumbers

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    '''
    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None
    '''


class PhotoAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView
):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumbers
    search_fields = ('user__username', 'content')
    ordering_fields = ('user__username', 'timestamp')

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        print(request.user)
        qs = Photo.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



