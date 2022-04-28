from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegisterUserForm
from .models import Users, Paymentgateway
from django.contrib.auth import login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import sys
import json

# Create your views here.

@csrf_exempt
def signup(request):
	form = RegisterUserForm(request.POST)
	user = form.save()
	user = json.loads(request.body.decode('utf8').replace("'", '"'))
	if form.is_valid():
		print(user)
		login(request, user)
		params = {
			'name': user['name'],
			'email': user['email'],
			'phone': user['phone'],
			'address': user['address'],
			'shipping_address': user['shippingAddress'],
			'referral_token': user['referralToken'],
			'wallet_amount': 0,
			'role': 'buyer',
			'password': user['password']
		}
		user = Users.objects.create_user(params)
		# print("User created", file=sys.stderr)
		return JsonResponse({'user_id': user.uid, 'status': 'Registration successful.'})
	# print(request.body, file=sys.stderr)
	return JsonResponse({'status': 'Unsuccessful registration. Invalid information.'})

