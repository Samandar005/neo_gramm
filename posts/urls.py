from django.urls import path
from . import views


app_name='posts'

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), 'create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), 'update'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), 'detail'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), 'delete'),
]