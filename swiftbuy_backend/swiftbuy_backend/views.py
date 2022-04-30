from ast import Constant
from datetime import datetime
import json
from django.shortcuts import render, redirect
from http import HTTPStatus
from django.http import JsonResponse
from user.models import Users, Product, Transaction, Orders, Addmoney, Incart, Notification, Wishlist, Paymentgateway
from .forms import AddMoneyForm
from django.contrib.auth.decorators import login_required
import sys
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Value, CharField, Sum, FloatField
from itertools import chain
import json
import numpy as np

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		advertised_products = Product.objects.filter(advertised=1).values()
		for p in advertised_products :
			p['images'] = p['images'][1:-1].replace('\\', '').split(',')[0].strip('"').strip('\\').strip('"')
		return JsonResponse({'status': 'success', 'results': list(advertised_products)[:100]}, status=HTTPStatus.OK)
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
		orders_list = list(Transaction.objects.filter(buyer_id=request.user.uid).all().values_list('order_id', flat=True))
		buy_txns = Product.objects.filter(transaction__order_id__in=orders_list).annotate(amount=F('discount')*F('transaction__quantity')).annotate(type=Value("Debited: Bought An Item", CharField())).values_list('type', 'amount')
		buy_ts = Orders.objects.filter(order_id__in=orders_list).values_list('trasaction_time')
		buy_txns = [list((zipped[0][0], zipped[0][1], zipped[1][0])) for zipped in zip(buy_txns, buy_ts)]
		sell_txns = Product.objects.filter(transaction__seller_id=request.user.uid).annotate(amount=F('discount')*F('transaction__quantity')).annotate(type=Value("Credited: Sold An Item", CharField())).values_list('type', 'amount')
		sell_ts = Orders.objects.filter(order_id__in=orders_list).values_list('trasaction_time')
		sell_txns = [list((zipped[0][0], zipped[0][1], zipped[1][0])) for zipped in zip(sell_txns, sell_ts)]
		add_txns = Addmoney.objects.filter(user_id=request.user.uid).annotate(type=Value("Added Money to Wallet", CharField())).values_list('type', 'amount', 'timestamp')
		txns = list(chain(buy_txns, sell_txns, add_txns))
		txns.sort(key=lambda x: x[2], reverse=True)
		wallet_amount = Users.objects.filter(uid=request.user.uid).values('wallet_amount')[0]['wallet_amount']
		return JsonResponse({'status': 'success', 'results': txns, 'wallet_amount': wallet_amount}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

@csrf_exempt
def addmoney(request):
	if request.user.is_authenticated:
		info = json.loads(request.body.decode('utf8').replace("'", '"'))
		form = AddMoneyForm({'amount': info['amount'], 'payment_gateway': info['payment_method']})
		if form.is_valid():
			params = {
				'id': np.random.randint(1000, 100000),
				'user_id': request.user.uid,
				'amount': info['amount'],
				'payment_id': info['payment_method'],
				'timestamp': datetime.now()
			}
			Addmoney.objects.create(**params)
			Users.objects.filter(uid=request.user.uid).update(wallet_amount=Users.objects.filter(uid=request.user.uid).values('wallet_amount')[0]['wallet_amount'] + int(info['amount']))
			return JsonResponse({'status': 'success', 'results': 'Money added successfully.'}, status=HTTPStatus.OK)
		else :
			return JsonResponse({'status': 'failure', 'results': 'Money not added.'}, status=HTTPStatus.BAD_REQUEST)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

@csrf_exempt
def cart(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			product_details = Product.objects.select_related('incart').filter(incart__buyer_id=request.user.uid).values()
			total_amount = list(Incart.objects.filter(buyer_id=request.user.uid).aggregate(total=Sum(F('quantity')*F('product__discount'), output_field=FloatField())).values())[0]
			return JsonResponse({'status': 'success', 'cart_products': list(product_details), 'total_amount': total_amount}, status=HTTPStatus.OK)
		elif request.method == 'POST':
			info = json.loads(request.body.decode('utf-8').replace("'", '"'))
			params = {
				'id': np.random.randint(1000, 10000),
				'buyer_id': request.user.uid,
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

@csrf_exempt
def order(request):
	if request.user.is_authenticated:
		cart_products = Incart.objects.filter(buyer_id=request.user.uid).values()
		total_amount = list(Incart.objects.filter(buyer_id=request.user.uid).aggregate(total=Sum(F('quantity')*F('product__discount'), output_field = FloatField())).values())[0]
		if total_amount is None : total_amount = 0
		new_balance = Users.objects.filter(uid=request.user.uid).values()[0]['wallet_amount'] - total_amount
		info = json.loads(request.body.decode('utf-8').replace("'", '"'))
		payment_id = int(info['payment_id'])
		if payment_id == 4 :
			if new_balance < 0 :
				return JsonResponse({'status': 'failure', 'results': 'Insufficient balance in wallet, please choose a different payment method or add money to your wallet.'}, status=411)
			Users.objects.filter(uid=request.user.uid).update(wallet_amount=new_balance)
		params = {
			'order_id': np.random.randint(20000, 100000),
			'user_id': request.user.uid,
			'payment_id': payment_id,
			'amount': total_amount,
			'trasaction_time': datetime.now()
		}
		Orders.objects.create(**params)
		order_id = Orders.objects.filter(user_id=request.user.uid, trasaction_time=params['trasaction_time'])
		
		for product in cart_products:
			seller_id = Product.objects.filter(product_id=product['product_id']).values('seller_id')[0]['seller_id']
			params = {
				'id': np.random.randint(200, 20000),
				'seller_id': seller_id,
				'buyer_id': request.user.uid,
				'order_id': order_id.values()[0]['order_id'],
				'product_id': product['product_id'],
				'quantity': product['quantity']
			}
			print(params)
			new_quantity = Product.objects.filter(product_id=product['product_id']).values()[0]['quantity_available'] - product['quantity']
			if new_quantity < 0 :
				return JsonResponse({'status': 'failure', 'results': 'Insufficient quantity in stock.'}, status=415)
			Transaction.objects.create(**params)
			Incart.objects.filter(buyer_id=request.user.uid).delete()
			Users.objects.filter(uid=seller_id).update(wallet_amount=Users.objects.filter(uid=seller_id).values('wallet_amount')[0]['wallet_amount'] + product['quantity'] * Product.objects.filter(product_id=product['product_id']).values()[0]['discount'])
			Product.objects.filter(product_id=product['product_id']).update(quantity_available=new_quantity)
			Notification.objects.create(user_id=seller_id, notif_text="You just sold " + str(product['quantity']) + " " + Product.objects.filter(product_id=product['product_id']).values()[0]['name'] + ".", notif_timestamp=datetime.now(), seen=0)
	
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

	



