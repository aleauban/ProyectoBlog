from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

# Create your views here.

def inicio (request):
    return render (request, 'AppBlog/padre.html')

def about (request):
    return render (request, 'AppBlog/about.html')

class PostList(ListView):
    model = Post
    template_name = "AppBlog/post.html"

class PostDetalle(DetailView):
    model = Post
    template_name = "AppBlog/post_detalle.html"
