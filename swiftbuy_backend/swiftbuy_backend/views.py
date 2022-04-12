from django.shortcuts import render, redirect
from .models import Fruit

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

