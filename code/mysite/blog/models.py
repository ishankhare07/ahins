from django.db import models
from core.models import User


class BlogPost(models.Model):
    publisher = models.ForeignKey('core.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False, default='Untitled')
    is_published = models.BooleanField(default=False)
    published_on = models.DateField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
