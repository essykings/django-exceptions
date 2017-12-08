from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PostSerializer
from .models import Post
from .utils import PostUnavailable

# Create your views here.


class PostsList(APIView):
    """
    List all Posts, or create a new Post.
    """

    def get(self, request, format=None):
        Posts = Post.objects.all()
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        print serializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetail(APIView):
    """
    Retrieve, update or delete a Post instance.
    """

    def get_object(self, pk):
        return Post.objects.get(pk=pk)
        # try:
        #     return Post.objects.get(pk=pk)
        # except Post.DoesNotExist:
        #     raise PostUnavailable

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
