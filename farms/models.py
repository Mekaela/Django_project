from django.db import models
from django.utils.text import slugify 
# from django.contrib.gis.db import models as geomodels

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

# class Block(models.Model):
#     farm = models.ForeignKey(Farm, related_name="blocks", on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     area = geomodels.PolygonField(srid=4326)
    # ...other block fields