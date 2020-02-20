from django.contrib import admin

# Register your models here.
from .models import Photo


class PhotoDetails(admin.ModelAdmin):
    list_display = ("user", "image", "content", "timestamp")
    list_filter = ("user", )


admin.site.register(Photo, PhotoDetails)