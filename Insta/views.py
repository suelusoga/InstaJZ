from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from Insta.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HelloWorld(TemplateView):
    template_name = 'test.html'


class PostsView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
