from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, View
from .forms import PostForm
from .models import Post
from django.db.models import Q, Count
from django.views.generic.edit import FormMixin
from comments.forms import CommentForm
from django.http import JsonResponse


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
            posts = posts.annotate(comment_count=Count('comments')).order_by('-comment_count')
        else:
            posts = posts.order_by('-created_at')

        return posts

class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posts = self.object
            comment.user = self.request.user
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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


class LikePostView(View):
    def post(self, request, post_id):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Login required'}, status=401)

        try:
            post = Post.objects.get(id=post_id)
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                liked = False
            else:
                post.likes.add(request.user)
                liked = True

            return JsonResponse({
                'liked': liked,
                'likes_count': post.likes.count()
            })
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)