from django.db import models
from .base_models import BaseModel
from django.shortcuts import reverse
from django.conf import settings


class Post(BaseModel):
    image = models.ImageField(upload_to='posts/')
    caption = models.CharField(max_length=50)
    hashtags = models.CharField(max_length=255)
    likes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='posts')

    def get_detail_url(self):
        return reverse('posts:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('posts:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('posts:update', args=[self.pk])


    @property
    def author_full_name(self):
        return self.author.full_name if self.author else ''

    def __str__(self):
        return f"{self.caption}"



