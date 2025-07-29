from django.shortcuts import render
from .models import FarmOperation
from farms.models import Farm
from crops.models import Crop
from users.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@login_required(login_url="/users/login/")
def ops_list(request):
    operations = FarmOperation.objects.all().order_by('-date')
    return render(request, 'farm_operations/ops_list.html', { 'operation': operations})

@login_required(login_url="/users/login/")
def op_page(request, slug):
    operation = FarmOperation.objects.get(slug=slug)
    return render(request, 'farm_operations/op_page.html', { 'operation': operation})

@login_required(login_url="/users/login/")
def op_new(request):
    farms = Farm.objects.all()
    crops = Crop.objects.all()
    User = get_user_model()
    users = User.objects.all()
    objects = {
        'farms': farms,
        'crops': crops, 
        'users': users, 
    }
    return render(request, 'farm_operations/op_new.html', objects)