from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.utils.timezone import now
from django.contrib.auth.models import User

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
    para1 = models.CharField(max_length=100)
    para2 = models.CharField(max_length=100)
    para3 = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    

class SubCategory(models.Model):
    Category = models.ForeignKey(Category,related_name="catname",on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_category_name
    
class Blog(models.Model):
    Category = models.ForeignKey(Category,related_name="cat_name",on_delete=models.CASCADE)
    SubCategory = models.ForeignKey(SubCategory,related_name="sub_cat_name",on_delete=models.CASCADE)
    title = models.CharField(max_length=255,default="title")
    heading = models.CharField(max_length=255,default="author")
    new_slug = AutoSlugField(populate_from="heading",unique=True,null=True,default=None,max_length=255)
    image = models.ImageField(upload_to="static/images")
    image1 = models.ImageField(upload_to="static/images",blank=True,null=True)
    author = models.CharField(max_length=255,default="heading")
    content = models.TextField()
    content1 = models.TextField()
    iframe = models.URLField(blank=True,null=True,max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)    

    def total_like(self):
        return self.like.count()
    
    def total_comment(self):
        return self.comment.count()
    
    def __str__(self):
        return self.author
    

class BlogComments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    time = models.DateTimeField(default=now)

    def __str__(self):
        return  self.comment[0:10]
    