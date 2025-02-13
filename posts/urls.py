from django.urls import path
from . import views


app_name='posts'

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('posts/<int:pk>/like/', views.LikePostView.as_view(), name='toggle_like'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
]