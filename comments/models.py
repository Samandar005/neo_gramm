from django.db import models
from django.conf import settings
from posts.base_models import BaseModel
from posts.models import Post

class Comments(BaseModel):
    comments = models.CharField(max_length=255)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.comments} by {self.user.full_name}"
