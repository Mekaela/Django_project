from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date_added = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title