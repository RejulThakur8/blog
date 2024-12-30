from django.urls import path,include
from blog_app import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('category/',views.category,name="category"),
    path('explore/',views.explore,name="explore"),
    path('bloghome/',views.bloghome,name="bloghome"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
]
