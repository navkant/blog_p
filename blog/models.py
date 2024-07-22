from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False, null=False)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=False, blank=False, related_name='blogs', on_delete=models.CASCADE)
    image_url = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.title

    @property
    def is_latest(self):
        return timezone.now() - self.created < timedelta(days=1)

    @property
    def author_name(self):
        return self.author.first_name