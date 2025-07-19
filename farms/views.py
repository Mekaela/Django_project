from django.shortcuts import render, redirect
from .models import Farm
from django.contrib.auth.decorators import login_required
from .forms import FarmForm

# Create your views here.
def farms_list(request):
    farms = Farm.objects.all().order_by('-date')
    return render(request, 'farms/farms_list.html', { 'farms': farms})

def farm_page(request, slug):
    farm = Farm.objects.get(slug=slug)
    return render(request, 'farms/farm_page.html', { 'farm': farm})

@login_required(login_url="/users/login/")
def farm_new(request):
    if request.method == "POST":
        form = FarmForm(request.POST)
        print('here')
        if form.is_valid():
            print('inside form valid')
            # Access cleaned data
            farm = form.save()
            print(farm.name, farm.size_hectares, farm.slug, farm.farm_lat, farm.farm_long)
        # If not valid, the invalid form with errors will be rendered
        # return redirect('farm', slug=farm.slug)
    else:
        print('else')
        form = FarmForm()
    return render(request, 'farms/farm_new.html', {'form': form})