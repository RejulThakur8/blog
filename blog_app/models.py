from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=100, unique=True)
    alter_phone_number = models.CharField(max_length=100)
    user_bio = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to="statics/profile")
    user_address = models.TextField()
    user_city = models.CharField(max_length=50)
    user_state = models.CharField(max_length=50)
    user_country = models.CharField(max_length=50)
    user_zipcode = models.CharField(max_length=50)