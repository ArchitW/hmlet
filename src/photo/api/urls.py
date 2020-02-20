from django.conf.urls import url
from .views import (
PhotoListSearchAPIView,
)

urlpatterns = [
    url(r'^$', PhotoListSearchAPIView.as_view()),
  #  url(r'^create/$', PhotoListAPIView.as_view()),
   # url(r'^(?P<id>)/$', PhotoDetailAPIView.as_view()),
]
