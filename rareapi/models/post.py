from django.db import models
from .user import User


class Post(models.Model):

    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    approved = models.BinaryField()
    rare_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
