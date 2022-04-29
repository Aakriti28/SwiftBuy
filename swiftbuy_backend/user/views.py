from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegisterUserForm
from .models import Users, Paymentgateway
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

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
	form = RegisterUserForm({'name': params['name'], 'email': params['email'], 'phone': params['phone'], 'address': params['address'], 'shipping_address': params['shipping_address'], 'referral_token': params['referral_token'], 'giver_token': user_info['referralToken'], 'password1': params['password'], 'password2': user_info['cpassword']})
	if form.is_valid() and form.referral_token_is_valid() and params['password'] == user_info['cpassword']:
		user = form.save()
		login(request, user)
		# user = Users.objects.create_user(params)
		return JsonResponse({'user_id': user.uid, 'status': 'Registration successful.'})
	print(form.errors)
	return JsonResponse({'status': 'Unsuccessful registration. Invalid information.'})

@csrf_exempt
def mylogin(request):
	user_info = json.loads(request.body.decode('utf8').replace("'", '"'))
	user = authenticate(request, username=user_info['email'], password=user_info['password'])
	if user is not None:
		login(request, user)
		return JsonResponse({'status': 'success'})
	else:
		if Users.objects.filter(email=user_info['email'], password=user_info['password']).exists():
			user = Users.objects.get(email=user_info['email'], password=user_info['password'])
			login(request, user)
			request.session['user_id'] = user.uid
			request.session.modified = True
			return JsonResponse({'status': 'success'})
	return JsonResponse({'status': 'failure'})

@csrf_exempt
def mylogout(request):
	logout(request)
	try:
		del request.session['user_id']
		request.session.flush()
	except KeyError:
		pass
	return JsonResponse({'status': 'Logout successful.'})

