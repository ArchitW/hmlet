from django.db import models
from django.conf import settings


def upload_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
