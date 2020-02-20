from rest_framework import serializers
from photo.models import Photo


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'user',
            'content',
            'image'
        ]

    def validate_content(self, value):
        pass

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or Image is required.")
        return data
