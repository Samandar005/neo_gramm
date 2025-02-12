from django.db import models
from .base_models import BaseModel


class Posts(BaseModel):
    image = models.ImageField(upload_to='posts/'),
    caption = models.CharField(max_length=50),
    hashtags = models.CharField(max_length=50),
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.caption}"

