from django.shortcuts import render, redirect
from http import HTTPStatus
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
		'role': user_info['role'],
		'password': user_info['password']
	}
	form = RegisterUserForm({'name': params['name'], 'email': params['email'], 'phone': params['phone'], 'address': params['address'], 'shipping_address': params['shipping_address'], 'referral_token': params['referral_token'], 'giver_token': user_info['referralToken'], 'password1': params['password'], 'password2': user_info['cpassword'], 'role': params['role']})
	if form.is_valid() and form.referral_token_is_valid() and params['password'] == user_info['cpassword']:
		user = form.save()
		login(request, user)
		# user = Users.objects.create_user(params)
		return JsonResponse({'results': user.uid, 'status': 'success'}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'failure', 'results': form.errors}, status=HTTPStatus.BAD_REQUEST)

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
			return JsonResponse({'status': 'success'}, status=HTTPStatus.OK)
	return JsonResponse({'status': 'auth_failure'}, status=HTTPStatus.UNAUTHORIZED)

@csrf_exempt
def mylogout(request):
	# print(request.user.is_authenticated, file=sys.stderr)
	logout(request)
	return JsonResponse({'status': 'success'}, status=HTTPStatus.OK)

