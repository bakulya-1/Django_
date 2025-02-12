from django.shortcuts import render, HttpResponse, Post
import random


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


def post_detail_view(request, post_title):
    post = Post.objects.get(title=post_title)
    return render(request, "posts/post_detail.html", context={"post":  post})



