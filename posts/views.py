from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import PostForm
from .models import Post
from django.db.models import Q


class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.all()
        search_query = self.request.GET.get('search', '')
        hashtag_filter = self.request.GET.get('hashtag', '')
        order_option = self.request.GET.get('order', 'Latest')

        if search_query:
            posts = posts.filter(
                Q(caption__icontains=search_query) |
                Q(hashtags__icontains=search_query)
            )

        if hashtag_filter and hashtag_filter.lower() != 'all':
            posts = posts.filter(hashtags__icontains=hashtag_filter)

        if order_option == 'Most Liked':
            posts = posts.order_by('-likes')
        elif order_option == 'Most Commented':
            posts = posts.order_by('-comment_count')
        else:
            posts = posts.order_by('-created_at')
        return posts



class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('home')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'
    context_object_name = 'post'

    def get_success_url(self):
        return self.object.get_detail_url()

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post-delete-confirm.html'
    success_url = reverse_lazy('home')
