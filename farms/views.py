from django.shortcuts import render, redirect
from .models import Farm, Block
from crops.models import Crop
from django.contrib.auth.decorators import login_required
from .forms import FarmForm
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from django.contrib.gis.geos import GEOSGeometry

@login_required(login_url="/users/login/")
def farms_list(request):
    farms = Farm.objects.all().order_by('-date')
    crops = Crop.objects.all()
    context = {
        'farms': farms,
        'crops': crops, 
    }
    return render(request, 'farms/farms_list.html', context)

@login_required(login_url="/users/login/")
def farm_page(request, slug):
    farm = Farm.objects.get(slug=slug)
    return render(request, 'farms/farm_page.html', { 'farm': farm})

@login_required(login_url="/users/login/")
def farm_new(request):
    if request.method == "POST":
        form = FarmForm(request.POST)
        if form.is_valid():
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

@login_required(login_url="/users/login/")
def plots_for_farm(request, farm_id):
    plots = Block.objects.filter(farm_id=farm_id).values('id', 'name', 'area', 'farm_id')
    # Convert to GeoJSON format
    for plot in plots:
        plot['area'] = json.loads(plot['area'].geojson) # Convert GEOSGeometry to GeoJSON       
    # Return as JSON response
    return JsonResponse(list(plots), safe=False)

