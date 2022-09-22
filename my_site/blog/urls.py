from django.urls import path
from . import views

urlpatterns = [
    path("", views.startingPage, name="starting-page"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.postDetail, name="post-detail-page"), #/posts/my-first-post
]