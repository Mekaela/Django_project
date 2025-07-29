from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# To add crop varieties: 
# class Variety(models.Model):
#     crop = models.ForeignKey(Crop, related_name='varieties', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.crop.name} - {self.name}"