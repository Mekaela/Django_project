from django.urls import path
from . import views

app_name = 'farms'

urlpatterns = [
    path('', views.farms_list, name="list"),
    path('new-farm/', views.farm_new, name="new-farm"),
    path('<slug:slug>', views.farm_page, name="farm"),
    path('plots-for-farm/<int:farm_id>/', views.plots_for_farm, name='plots_for_farm'),
]