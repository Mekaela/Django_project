from django.db import models

class FarmOperation(models.Model):
    record_type = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    farm = models.ForeignKey('farms.Farm', related_name='farm', on_delete=models.CASCADE)

    def __str__(self):
        return self.title