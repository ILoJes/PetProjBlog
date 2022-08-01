from rest_framework import serializers
from ..models import Post


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug']
