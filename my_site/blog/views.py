from django.shortcuts import render
from datetime import date
from .models import Post

all_posts = [
    
]  # type: ignore

def get_date(post):
    return post["date"]

# Create your views here.

def startingPage(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def postDetail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post":identified_post
    })