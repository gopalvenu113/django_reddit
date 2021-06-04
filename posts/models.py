from django.db import models

# Create your models here.


class Post(models.Model):
    # user = models.ForeignKey(User)
    post_name = models.CharField(max_length=100)
    post_data = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(null=True, default=0)
    # community = models.ForeignKey(Community)


class Comment(models.Model):
    # user = models.ForeignKey(User)
    comment_data = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(null=True, default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
