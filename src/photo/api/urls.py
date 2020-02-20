from django.conf.urls import url
from .views import (
    PhotoAPIView,
    PhotoCreateAPIView,
    PhotoDetailAPIView,
)

urlpatterns = [
    url(r'^$', PhotoAPIView.as_view()),
    url(r'^create/$', PhotoCreateAPIView.as_view()),
    url(r'^(?P<id>)/$', PhotoDetailAPIView.as_view()),
]
