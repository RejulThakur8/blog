from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=100, unique=True)
    alter_phone_number = models.CharField(max_length=100)
    user_bio = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to="static/profile")
    user_address = models.TextField()
    user_city = models.CharField(max_length=50)
    user_state = models.CharField(max_length=50)
    user_country = models.CharField(max_length=50)
    user_zipcode = models.CharField(max_length=50)

class Authenticate(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20,default=5234)

    def __str__(self):
        return self.username

class Nav(models.Model):
    image = models.ImageField(upload_to="static/images", height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.title