from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegisterUserForm
from .models import Users
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def signup(request):
	form = RegisterUserForm(request.POST)
	if form.is_valid():
		user = form.save()
		login(request, user)
		params = {
			'name': user.name,
			'email': user.email,
			'phone': user.phone,
			'address': user.address,
			'shipping_address': user.shipping_address,
			'referral_token': user.referral_token,
			'wallet_amount': 0,
			'role': 'buyer'
		}
		user = Users.objects.create(**params)
		return JsonResponse({'user_id': user.id, 'status': 'Registration successful.'})
	messages.error(request, "Unsuccessful registration. Invalid information.")
	return JsonResponse({'status': 'Unsuccessful registration. Invalid information.'})

