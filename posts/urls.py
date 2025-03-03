from django.urls import path
from . import views


app_name='posts'

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('likes/<int:post_id>/like/', views.LikePostView.as_view(), name='toggle_like'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
]