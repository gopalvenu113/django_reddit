from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from posts.filters import PostFilterSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.serializers import PostSerializer, PostCreateSerializer, PostNamesListSerializer


# Create your views here.


# def index(request):
#     return HttpResponse('This is Sample API')


def posts_list(request):
    posts = Post.objects.all()
    return render(request, template_name='list_of_posts.html', context={'posts': posts, 'is_retrieve': False})

def posts_retrieve(request, pk):
    posts = Post.objects.filter(id=pk)
    return render(request, template_name='list_of_posts.html', context={'posts': posts, 'is_retrieve': True})


# def create(request):
#     return render(request, template_name='create_post.html')

# def create_post(request):
#     data = request.POST
#     posts = Post.objects.create(post_name=data['Post name'], post_data=data['Post data'])
#     return render(request, template_name='list_of_posts.html', context={'posts': posts, 'is_retrieve': True})



class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = PostFilterSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        serializer_mapping = {
            'list':PostSerializer,
            'retreive': PostSerializer,
            'create': PostCreateSerializer,
            'list_post': PostNamesListSerializer
        }
        return serializer_mapping.get(self.action, PostSerializer)

    def list(self, request):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @action(methods=['get'], name='list_post', detail=False)
    def list_post(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)