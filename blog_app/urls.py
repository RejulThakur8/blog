from django.urls import path,include
from blog_app import views
from .views import *

urlpatterns = [
    path('home/',HomeListView.as_view(),name="home"),
    path('comment/',views.blogcomments,name="comment"),
    path('explore/',views.explore,name="explore"),
    path('category/',views.category,name="category"),
    path('create_blog/',views.createblog,name="createblog"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('logout/',views.signout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('bookmark/',views.bookmark,name="bookmark"),
    path('bloghome/<slug>',views.bloghome,name="bloghome"),
    path('search/',views.search,name="search"),
]
