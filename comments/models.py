from django.db import models
from posts.base_models import BaseModel
from posts.models import Posts


class Comments(BaseModel):
    comments = models.CharField(max_length=255)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
