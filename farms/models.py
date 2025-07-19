from django.db import models
from django.utils.text import slugify 

class Farm(models.Model):
    name = models.CharField(max_length=75)
    # change to pointfield, but needs install
    size_hectares = models.CharField(max_length=20)
    farm_lat = models.CharField(max_length=20)
    farm_long = models.CharField(max_length=20)

    slug = models.SlugField(unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Farm, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

