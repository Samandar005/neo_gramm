from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import PostForm
from .models import Posts


class HomePageView(ListView):
    model = Posts
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Posts
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('home')

class PostUpdateView(UpdateView):
    model = Posts
    form_class = PostForm
    template_name = 'posts/post_create.html'
    context_object_name = 'post'

    def get_success_url(self):
        return self.object.get_detail_url()

class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'post/post-delete-confirm.html'
    success_url = reverse_lazy('home')
