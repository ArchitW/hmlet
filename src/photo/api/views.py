from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Photo
from .serializers import PhotoSerializers


class PhotoListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Photo.objects.all()
        serializer = PhotoSerializers(qs, many=True)
        return Response(serializer.data)