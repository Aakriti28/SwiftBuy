from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegisterUserForm
from .models import Users
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def homepage(request):
	# return render(request, 'home.html')
	return JsonResponse({'data': 'Hello'})

def signup(request):
	form = RegisterUserForm(request.POST)
	if form.is_valid():
		user = form.save()
		login(request, user)
		messages.success(request, "Registration successful." )
		return redirect('home')
	messages.error(request, "Unsuccessful registration. Invalid information.")

