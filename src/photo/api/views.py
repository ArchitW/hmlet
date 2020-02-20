from rest_framework.views import APIView
from rest_framework import generics

from rest_framework.response import Response

from ..models import Photo
from .serializers import PhotoSerializer


class PhotoListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Photo.objects.all()
        serializer = PhotoSerializer(qs, many=True)
        return Response(serializer.data)


class PhotoAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        qs =  Photo.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class PhotoCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    lookup_field = 'id'
