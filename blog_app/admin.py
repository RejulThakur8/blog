from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.



class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number','alter_phone_number','user_bio','user_image','user_address','user_city','user_state','user_country','user_zipcode'),
                }),
    )

class NavAdmin(admin.ModelAdmin):
    list_display = ["image","title","caption"]

class AuthenticateAdmin(admin.ModelAdmin):
    list_display = ["username","email","password","phone_number"]

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Nav,NavAdmin) 
admin.site.register(Authenticate,AuthenticateAdmin) 