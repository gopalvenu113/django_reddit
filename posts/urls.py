from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
]
