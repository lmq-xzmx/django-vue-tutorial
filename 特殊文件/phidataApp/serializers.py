from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['question', 'created_at', 'response']
