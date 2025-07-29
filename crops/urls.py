from django.urls import path
from . import views

app_name = 'crops'

urlpatterns = [
    path('', views.crops_list, name="list"),
]