from rest_framework.utils import field_mapping
from posts.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    community_name = serializers.CharField(source='community.name')
    username = serializers.CharField(source='user.username')
    calculated_field = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ['post_name', 'username', 'created_time', 'votes', 'community_name', 'calculated_field']
    
    def get_calculated_field(self, instance):
        return 'this is calculated field'


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class PostNamesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['post_name']