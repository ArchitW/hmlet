from django.conf.urls import url
from .views import (
    PhotoAPIView,
    #PhotoDetailAPIView,
)

urlpatterns = [
    url(r'^$', PhotoAPIView.as_view()),
    #url(r'^(?P<id>\d+)/$', PhotoDetailAPIView.as_view()),
]
