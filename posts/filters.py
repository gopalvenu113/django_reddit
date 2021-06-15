import django_filters
from posts.models import Post


class PostFilterSet(django_filters.FilterSet):
    post_name = django_filters.CharFilter(field_name='post_name')
    user_name = django_filters.CharFilter(field_name='user__username')

    class Meta:
        model = Post
        fields = []