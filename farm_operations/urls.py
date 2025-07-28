from django.urls import path
from . import views

app_name = 'farm_operations'

urlpatterns = [
    path('', views.ops_list, name="list"),
    path('new-op/', views.op_new, name="new-op"),
    path('<slug:slug>', views.op_page, name="page"),
]