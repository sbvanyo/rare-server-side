from django.db import models
from .user import User
from .post import Post

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_posts")
    content = models.CharField(max_length=100)
    created_on = models.DateField(auto_now=False)
