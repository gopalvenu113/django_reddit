from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.


# def index(request):
#     return HttpResponse('This is Sample API')


def posts_list(request):
    posts = Post.objects.all()
    return render(request, template_name='list_of_posts.html', context={'posts': posts}) 