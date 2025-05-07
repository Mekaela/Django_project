from django.shortcuts import render

from django.shortcuts import render
from .models import Farm
from django.contrib.auth.decorators import login_required

# Create your views here.
def farms_list(request):
    farms = Farm.objects.all().order_by('-date')
    return render(request, 'farms/farms_list.html', { 'farms': farms})

def farm_page(request, slug):
    farm = Farm.objects.get(slug=slug)
    return render(request, 'farms/farm_page.html', { 'farm': farm})

@login_required(login_url="/users/login/")
def farm_new(request):
    return render(request, 'farms/farm_new.html')
