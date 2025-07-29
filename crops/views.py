from django.shortcuts import render
from .models import Crop
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required(login_url="/users/login/")
def crops_list(request):
    crops = Crop.objects.all().order_by('-date')
    return JsonResponse(list(crops), safe=False)