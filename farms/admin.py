from django.contrib import admin
from .models import Farm, Block
from django.contrib.gis.admin import GISModelAdmin

# Register your models here.
admin.site.register(Farm)
admin.site.register(Block)
class BlockAdmin(GISModelAdmin):
    list_display = ('farm','name', 'area')