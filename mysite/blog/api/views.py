from rest_framework import generics
from ..models import Post
from .serializers import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = SubjectSerializer
