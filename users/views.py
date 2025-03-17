from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { "form": form})

# def user_page(request, slug):
#     user = User.objects.get(slug=slug)
#     return render(request, 'users/user_page.html', { 'user': user})