from django.conf.urls import url
from .views import PostsList, PostDetail

urlpatterns = [
    url(r'^posts/$', PostsList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view()),
]
