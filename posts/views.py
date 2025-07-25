from django.shortcuts import render
from .models import Post
from farms.models import Farm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login/")
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts})

@login_required(login_url="/users/login/")
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', { 'post': post})

@login_required(login_url="/users/login/")
def post_new(request):
    farms = Farm.objects.all()
    return render(request, 'posts/post_new.html', {'farms': farms})