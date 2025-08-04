from django.shortcuts import render
from .models import FarmOperation
from .forms import FertilisationForm, IrrigationForm, PlantingForm, HarvestingForm, PesticideApplicationForm
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
    operation_type = request.GET.get('operation_type') or request.POST.get('operation_type')

    form = None
    form_classes = {
        'FERT': FertilisationForm,
        'IRR': IrrigationForm,
        'PLANT': PlantingForm,
        'HARV': HarvestingForm,
        'PEST': PesticideApplicationForm,
    }
    form_class = form_classes.get(operation_type)
    if request.method == 'POST':
        if not form_class:
            # Handle unsupported operation_type
            return render(request, 'error.html', {'message': 'Invalid operation type.'})

        # form = FertilisationForm(request.POST)
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'farm_operations/op_page.html', {'form': form, 'operation_type': operation_type}) 
    else:
        
        if form_class:
            form = form_class(initial={'operation_type': operation_type})
        else:
            form = None  # Or redirect or show an error

    return render(request, 'farm_operations/op_new.html', {'form': form, 'operation_type': operation_type})
    
    # farms = Farm.objects.all()
    # crops = Crop.objects.all()
    # User = get_user_model()
    # users = User.objects.all()
    # objects = {
    #     'farms': farms,
    #     'crops': crops, 
    #     'users': users, 
    # }
    # return render(request, 'farm_operations/op_new.html', objects)
