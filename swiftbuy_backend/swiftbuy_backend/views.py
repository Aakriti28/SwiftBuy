from ast import Constant
from datetime import datetime
import json
from django.shortcuts import render, redirect
from http import HTTPStatus
from django.http import JsonResponse
from user.models import Users, Product, Transaction, Orders, Addmoney, Incart, Notification, Wishlist
from .forms import AddMoneyForm
from django.contrib.auth.decorators import login_required
import sys
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Value, CharField, Sum
from itertools import chain
import json

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		advertised_products = Product.objects.filter(is_advertised=True)
		return JsonResponse({'status': 'success', 'results': list(advertised_products.values())}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

@csrf_exempt
def about(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			details = Users.objects.filter(uid=request.user.uid).values()[0]
			return JsonResponse({'status': 'success', 'results': details}, status=HTTPStatus.OK)
		elif request.method == 'POST':
			user = json.loads(request.body.decode('utf8').replace("'",'"'))['user']
			print(user)
			params = {
				'name': user['name'],
				'email': user['email'],
				'phone': user['phone'],
				'address': user['address'],
				'shipping_address': user['shipaddress']
			}
			print("params :",params)
			Users.objects.filter(uid=request.user.uid).update(**params)
			return JsonResponse({'status': 'success', 'results': 'Profile updated'}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

@csrf_exempt
def wallet(request):
	if request.user.is_authenticated:
		orders_list = list(Orders.objects.filter(user_id=request.user.uid).all().values_list('order_id', flat=True))
		buy_txns = Product.objects.filter(transaction__order_id__in=orders_list).annotate(amount=F('discount')*F('transaction__quantity')).annotate(type=Value("B", CharField())).values_list('type', 'amount')
		buy_ts = Orders.objects.filter(user_id=request.user.uid, order_id__in=orders_list).values_list('trasaction_time')
		buy_txns = [list((zipped[0][0], zipped[0][1], zipped[1][0])) for zipped in zip(buy_txns, buy_ts)]
		sell_txns = Product.objects.filter(transaction__seller_id=request.user.uid).annotate(amount=F('discount')*F('transaction__quantity')).annotate(type=Value("S", CharField())).values_list('type', 'amount')
		sell_ts = Orders.objects.filter(order_id__in=orders_list, transaction__seller_id=request.user.uid).values_list('trasaction_time')
		sell_txns = [list((zipped[0][0], zipped[0][1], zipped[1][0])) for zipped in zip(sell_txns, sell_ts)]
		add_txns = Addmoney.objects.filter(user_id=request.user.uid).annotate(type=Value("A", CharField())).values_list('type', 'amount', 'timestamp')
		txns = list(chain(buy_txns, sell_txns, add_txns))
		txns.sort(key=lambda x: x[2], reverse=True)
		return JsonResponse({'status': 'success', 'results': txns}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def addmoney(request):
	if request.user.is_authenticated:
		form = AddMoneyForm(request.POST)
		if form.is_valid():
			params = {
				'user_id': request.user.uid,
				'amount': form.cleaned_data['amount'],
				'payment_method': form.cleaned_data['payment_method'],
				'timestamp': datetime.now()
			}
			Addmoney.objects.create(**params)
			Users.objects.filter(uid=request.user.uid).update(wallet_amount=Users.objects.get(uid=request.user.uid).wallet_amount + form.cleaned_data['amount'])
			return JsonResponse({'status': 'success', 'results': 'Money added successfully.'}, status=HTTPStatus.OK)
		else :
			return JsonResponse({'status': 'failure', 'results': 'Money not added.'}, status=HTTPStatus.BAD_REQUEST)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def cart(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			product_details = Product.objects.filter(user_id=request.user.uid).select_related('incart').values()
			total_amount = Incart.objects.filter(user_id=request.user.uid).aggregate(total=Sum(F('quantity')*F('product__discount'))).values()[0]['total']
			return JsonResponse({'status': 'success', 'cart_products': list(product_details.values()), 'total_amount': total_amount}, status=HTTPStatus.OK)
		elif request.method == 'POST':
			info = json.loads(request.body.decode('utf-8').replace("'", '"'))
			params = {
				'user_id': request.user.uid,
				'product_id': info['product_id'],
				'quantity': info['quantity']
			}
			Incart.objects.create(**params)
			return JsonResponse({'status': 'success', 'results': 'Product added to cart.'}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def wishlist(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			wishlist_products = Wishlist.objects.filter(user_id=request.user.uid)
			return JsonResponse({'status': 'success', 'results': list(wishlist_products.values())})
		elif request.method == 'POST':
			info = json.loads(request.body.decode('utf-8').replace("'", '"'))
			params = {
				'user_id': request.user.uid,
				'product_id': info['product_id'],
			}
			Wishlist.objects.create(**params)
			return JsonResponse({'status': 'success', 'results': 'Product added to wishlist.'}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def order(request):
	if request.user.is_authenticated:
		cart_products = Incart.objects.filter(user_id=request.user.uid)
		total_amount = Incart.objects.filter(user_id=request.user.uid).aggregate(total=Sum(F('quantity')*F('product__discount'))).values()[0]['total']
		new_balance = Users.objects.get(uid=request.user.uid).wallet_amount - total_amount
		info = json.loads(request.body.decode('utf-8').replace("'", '"'))
		payment_id = info['payment_id']
		if payment_id == 4 :
			if new_balance < 0 :
				return JsonResponse({'status': 'failure', 'results': 'Insufficient balance in wallet, please choose a different payment method or add money to your wallet.'}, status=HTTPStatus.BAD_REQUEST)
			Users.objects.filter(id=request.user.uid).update(wallet_amount=new_balance)
		params = {
			'user_id': request.user.uid,
			'payment_id': payment_id,
			'amount': total_amount,
			'trasaction_time': info['transaction_time']
		}
		Orders.objects.create(**params)
		order_id = Orders.objects.filter(user_id=request.user.uid, transaction_time=info['transaction_time'])
		
		for product in cart_products:
			seller_id = Product.objects.get(id=product.product_id).seller_id
			params = {
				'seller_id': seller_id,
				'buyer_id': request.user.uid,
				'order_id': order_id,
				'product_id': product.product_id,
				'quantity': product.quantity
			}
			new_quantity = Product.objects.filter(id=product.product_id).values()[0]['quantity_available'] - product.quantity
			if new_quantity < 0 :
				return JsonResponse({'status': 'failure', 'results': 'Insufficient quantity in stock.'}, status=HTTPStatus.BAD_REQUEST)
			Transaction.objects.create(**params)
			Incart.objects.filter(user_id=request.user.uid).delete()
			Users.objects.filter(id=seller_id).update(wallet_amount=Users.objects.get(uid=seller_id).wallet_amount + product.quantity * Product.objects.get(id=product.product_id).price * (1 - Product.objects.get(id=product.product_id).discount))
			Product.objects.filter(id=product.product_id).update(quantity=new_quantity)
			Notification.objects.create(user_id=seller_id, message="You just sold " + str(product.quantity) + " " + Product.objects.get(id=product.product_id).name + ".", time=datetime.now(), seen=0)
	
		return JsonResponse({'status': 'success', 'results': 'Order placed successfully.'}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def notifications(request):
	if request.user.is_authenticated:
		uid = request.user.uid
		notifications = Notification.objects.filter(user_id=uid).order_by('-notif_timestamp')
		# print(list(notifications.values()), file=sys.stderr)
		return JsonResponse({'status': 'success', 'results': list(notifications.values())}, status=HTTPStatus.OK)
	else :
		print("Not authenticated", file=sys.stderr)
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

	



