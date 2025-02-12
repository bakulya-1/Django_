from django.shortcuts import render, HttpResponse
import random
from django.views.generic import ListView
from .models import Post


def test_view(request):
    return HttpResponse(f"Добро пожаловать на мою страницу:) {random.randint(1, 100)}")


def html_view(request):
    return render(request, "main.html")


def post_list_view(request):
    posts = Post.objects.all()
    print(posts)
    for post in posts:
        print(post.title, post.rate, post.content)
    return render(request, "posts/post_list.html", context={"posts": posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail.html", context={"post":  post})

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


