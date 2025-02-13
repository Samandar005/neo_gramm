from django.db import models
from .base_models import BaseModel
from django.shortcuts import reverse
from django.conf import settings
from django.utils.text import slugify


class Post(BaseModel):
    image = models.ImageField(upload_to='posts/')
    caption = models.CharField(max_length=50)
    hashtags = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    likes = models.ManyToManyField( settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.caption)
        super(Post, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('posts:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_delete_url(self):
        return reverse('posts:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('posts:update', args=[self.pk])

    @property
    def author_full_name(self):
        return self.author.full_name if self.author else ''

    def __str__(self):
        return f"{self.caption}"



