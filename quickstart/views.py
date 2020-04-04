from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def up_vote(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.popularity += 1
        post.save()
        return Response({'status': 'upvote increase'})

    @action(detail=True, methods=['get'])
    def down_vote(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.popularity -= 1
        post.save()
        return Response({'status': 'upvote decrease'})
        