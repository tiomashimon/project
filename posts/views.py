from django.shortcuts import render
from .models import PostModel


def posts(request):
    posts_list = PostModel.objects.all()
    return render(request, 'posts/posts.html', {'posts': posts_list})


def detail(request, id):
    post = PostModel.objects.get(id=id)
    return render(request, "posts/detail.html", {'post': post})
