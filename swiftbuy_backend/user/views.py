from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegisterUserForm
from .models import Users, Paymentgateway
from django.contrib.auth import login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import sys
import json
import random
import string

# Create your views here.

@csrf_exempt
def signup(request):
	user_info = json.loads(request.body.decode('utf8').replace("'", '"'))
	params = {
		'name': user_info['name'],
		'email': user_info['email'],
		'phone': user_info['phone'],
		'address': user_info['address'],
		'shipping_address': user_info['shipaddress'],
		'referral_token': ''.join(random.choices(string.ascii_lowercase + string.digits, k=32)).replace("'", '"'),
		'wallet_amount': 0,
		'role': 'buyer',
		'password': user_info['password']
	}
	form = RegisterUserForm(initial={'name': params['name'], 'email': params['email'], 'phone': params['phone'], 'address': params['address'], 'shipping_address': params['shipping_address'], 'referral_token': params['referral_token'], 'giver_token': user_info['referralToken']})
	if form.is_valid():
		user = form.save()
		login(request, user)
		user = Users.objects.create_user(params)
		# print("User created", file=sys.stderr)
		return JsonResponse({'user_id': user.uid, 'status': 'Registration successful.'})
	print("User not created", file=sys.stderr)
	print(form.errors)
	return JsonResponse({'status': 'Unsuccessful registration. Invalid information.'})

