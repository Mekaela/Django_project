from django.contrib import admin
from .models import FarmOperation, Fertilisation, Irrigation, Harvesting, Planting, PesticideApplication

# Register your models here.
admin.site.register(FarmOperation)
admin.site.register(Fertilisation)
admin.site.register(Irrigation)
admin.site.register(Harvesting)
admin.site.register(Planting)
admin.site.register(PesticideApplication)