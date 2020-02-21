from rest_framework import serializers,fields
from ..models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    flag = serializers.SerializerMethodField()


    class Meta:
        model = Photo
        fields = [
            'id',
            'user',
            'content',
            'image',
            'updated',
            'flag'

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

    def get_flag(self, data):
        content = data.content
        if content == "":
            content = None
        image = data.image
        if image == "":
            image = None
        if content is None or image is None:
            return "draft"
        return None
