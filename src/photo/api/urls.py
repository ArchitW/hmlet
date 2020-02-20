from django.conf.urls import url
from .views import (
    PhotoAPIView,
    PhotoCreateAPIView,
    PhotoDetailAPIView,
    PhotoUpdateAPIView
)

urlpatterns = [
    url(r'^$', PhotoAPIView.as_view()),
    url(r'^create/$', PhotoCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', PhotoDetailAPIView.as_view()),
    url(r'^(?P<id>\d+)/update/$', PhotoUpdateAPIView.as_view()),
]
