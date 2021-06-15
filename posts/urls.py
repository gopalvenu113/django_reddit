from django.urls import path, include
from posts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', views.PostViewset)

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:pk>', views.posts_retrieve, name='posts_retrieve'),
    # path('create', views.create, name='create'),
    # path('create_post', views.create_post, name='create_post')
    path('posts/', include(router.urls))
]
