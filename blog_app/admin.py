from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.



class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number','alter_phone_number','user_bio','user_address','user_city','user_state','user_country','user_zipcode'),
                }),
    )

class NavAdmin(admin.ModelAdmin):
    list_display = ["title","caption","para1","para2","para3","image"]

class AuthenticateAdmin(admin.ModelAdmin):
    list_display = ["username","email","password","phone_number"]

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title","heading","category","subcategory","subsubcategory","image"]

class BlogCommentsAdmin(admin.ModelAdmin):
    list_display = ["user","blog"]

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Nav,NavAdmin) 
admin.site.register(Authenticate,AuthenticateAdmin) 
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
admin.site.register(BlogComments,BlogCommentsAdmin)
admin.site.register(Logo)