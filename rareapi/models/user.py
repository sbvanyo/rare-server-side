from django.db import models

class User(models.Model):
  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    profile_image_url = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    created_on = models.DateField()
    active = models.BinaryField()
    is_staff = models.BooleanField(default=False)
    uid = models.CharField(max_length=50)
