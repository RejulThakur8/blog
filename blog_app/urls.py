from django.urls import path,include
from blog_app import views
from .views import *

urlpatterns = [
    path('',HomeListView.as_view(),name="home"),
    path('category/',CategoryBlogView.as_view(),name="category"),
    path('category/<int:pk>/',CategoryBlogView.as_view(),name="category-blog"),
    path('dashboard/',DashboardView.as_view(),name="dashboard"),
    path('comment/delete/<int:pk>/',CommentDeleteView.as_view(),name="delete-comment"),

    # function based view
    path('comment/',views.blogcomments,name="comment"),
    path('create_blog/',views.createblog,name="createblog"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('logout/',views.signout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('bloghome/<slug>',views.bloghome,name="bloghome"),
    path('search/',views.search,name="search"),
]
