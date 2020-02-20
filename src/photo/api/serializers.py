from rest_framework import serializers
from ..models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'id',
            'user',
            'content',
            'image',
            'updated'

        ]
        read_only_fields = ['user']

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if image is not None:
            pass
            #print(image)
        if content is None and image is None:
            raise serializers.ValidationError("Content or Image is required.")
        return data
