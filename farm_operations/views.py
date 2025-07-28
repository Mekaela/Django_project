from django.shortcuts import render
from .models import FarmOperation
from farms.models import Farm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'farm_operations/op_new.html', {'farms': farms})