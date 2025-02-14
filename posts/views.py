
from django.shortcuts import render, HttpResponse, redirect
import random
from django.views.generic import ListView
from posts.models import Post

from posts.forms import PostCreateForm


def test_view(request):
    return HttpResponse(f"Добро пожаловать на мою страницу:) {random.randint(1, 100)}")


def html_view(request):
    if request.method == "GET":
        return render(request, "main.html")
    else:
        return None


def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        print(posts)
        for post in posts:
            print(post.title, post.rate, post.content)
        return render(request, "posts/post_list.html", context={"posts": posts})



def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post":  post})

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


def post_create_view(request):
    if request.method == "GET":
        form = PostCreateForm()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        elif form.is_valid():
            image = form.cleaned_data.get("image")
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            post = Post.objects.create(image=image, title=title, content=content)
        if post:
            return redirect("/posts/")
        else:
            return HttpResponse("Post не был получен")




