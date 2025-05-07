from django.db import models

class Farm(models.Model):
    title = models.CharField(max_length=75)
    # change to pointfield, but needs install
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

