from django.db import models
from django.contrib.auth.models import User
from communities.models import Community

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=100)
    post_data = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(null=True, default=0)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_data = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(null=True, default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_data
