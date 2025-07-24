from django.shortcuts import render, redirect
from .models import Farm, Block
from django.contrib.auth.decorators import login_required
from .forms import FarmForm
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from django.contrib.gis.geos import GEOSGeometry

@login_required(login_url="/users/login/")
def farms_list(request):
    farms = Farm.objects.all().order_by('-date')
    return render(request, 'farms/farms_list.html', { 'farms': farms})

@login_required(login_url="/users/login/")
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

def block_create(request):
    print(f"Received {request.method} at {request.path}")
    if request.method == "POST":
        data = json.loads(request.body)
        name = data["name"]
        geom = data["area"]  # GeoJSON dictionary

        # Construct GEOSGeometry from GeoJSON
        polygon = GEOSGeometry(json.dumps(geom))

        paddock = Block.objects.create(
            name=name,
            area=polygon,
            farm= Farm.objects.get(pk=data.get("farm_id", 1))
        )
        return JsonResponse({"status": "ok", "id": paddock.id})
    return JsonResponse({"error": "POST required"}, status=400)