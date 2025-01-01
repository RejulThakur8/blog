from django.urls import path,include
from blog_app import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('explore/',views.explore,name="explore"),
    path('category/',views.category,name="category"),
    path('create-blog/',views.createblog,name="createblog"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('logout/',views.signout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('bookmark/',views.bookmark,name="bookmark"),
    path('bloghome/',views.bloghome,name="bloghome"),
]
