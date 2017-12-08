from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('created',)
        fields = ['id', 'name', 'description', 'created']
