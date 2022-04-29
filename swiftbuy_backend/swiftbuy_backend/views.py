from django.shortcuts import render, redirect
from http import HTTPStatus
from django.http import JsonResponse
from user.models import Users, Product, Transaction, Orders, Addmoney, Incart, Notification, Wishlist
from .forms import AddMoneyForm
from django.contrib.auth.decorators import login_required
import sys
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		advertised_products = Product.objects.filter(is_advertised=True)
		return JsonResponse({'status': 'success', 'results': advertised_products}, status=HTTPStatus.OK)
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

def wallet(request):
	if request.user.is_authenticated:
		transactions = Transaction.objects.all().raw('(SELECT (product.price * (1 - product.discount) * transaction.quantity * -1) AS amount, timestamp, "Bought" AS type FROM transaction NATURAL JOIN product, order WHERE order.id = transaction.order_id AND transaction.buyer_id = %s) UNION (SELECT (product.price * (1 - product.discount) * transaction.quantity) AS amount, timestamp, "Sold" AS type FROM transaction NATURAL JOIN product, order WHERE order.id = transaction.order_id AND transaction.seller_id = %s) UNION (SELECT amount, timestamp, "Added" AS type FROM add_money WHERE user_id = %s) ORDER BY timestamp DESC;', [request.user.uid, request.user.uid, request.user.uid])
		return JsonResponse({'status': 'success', 'results': list(transactions.values())}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def addmoney(request):
	if request.user.is_authenticated:
		form = AddMoneyForm(request.POST)
		if form.is_valid():
			params = {
				'user_id': request.user.uid,
				'amount': form.cleaned_data['amount'],
				'payment_method': form.cleaned_data['payment_method']
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
			product_details = Product.objects.all().raw('SELECT * FROM product natural join incart WHERE user_id = %s)', [request.user.uid])
			total_amount = Incart.objects.filter(user_id=request.user.uid).all().raw('SELECT SUM(product.price * (1 - product.discount) * quantity) AS total_amount FROM incart NATURAL JOIN product WHERE user_id = %s', [request.user.uid])
			return JsonResponse({'status': 'success', 'cart_products': list(product_details.values()), 'total_amount': total_amount.values()})
		elif request.method == 'POST':
			params = {
				'user_id': request.user.uid,
				'product_id': request.POST['product_id'],
				'quantity': request.POST['quantity']
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
			params = {
				'user_id': request.user.uid,
				'product_id': request.POST['product_id'],
			}
			Wishlist.objects.create(**params)
			return JsonResponse({'status': 'success', 'results': 'Product added to wishlist.'}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def order(request):
	if request.user.is_authenticated:
		cart_products = Incart.objects.filter(user_id=request.user.uid)
		total_amount = Incart.objects.filter(user_id=request.user.uid).all().raw('SELECT SUM(product.price * (1 - product.discount) * quantity) AS total_amount FROM incart NATURAL JOIN product WHERE user_id = %s', [request.user.uid])
		new_balance = Users.objects.get(uid=request.user.uid).wallet_amount - total_amount[0].total_amount
		payment_id = request.GET['payment_id']
		if payment_id == 4 :
			if new_balance < 0 :
				return JsonResponse({'status': 'failure', 'results': 'Insufficient balance in wallet, please choose a different payment method or add money to your wallet.'})
			Users.objects.filter(id=request.user.uid).update(wallet_amount=new_balance)
		params = {
			'user_id': request.user.uid,
			'payment_id': payment_id,
			'amount': total_amount[0].total_amount,
			'transaction_time': request.GET['transaction_time']
		}
		Orders.objects.create(**params)
		order_id = Orders.objects.filter(user_id=request.user.uid, transaction_time=request.GET['transaction_time'])
		
		for product in cart_products:
			seller_id = Product.objects.get(id=product.product_id).seller_id
			params = {
				'seller_id': seller_id,
				'buyer_id': request.user.uid,
				'order_id': order_id,
				'product_id': product.product_id,
				'quantity': product.quantity
			}
			new_quantity = Product.objects.get(id=product.product_id).quantity - product.quantity
			if new_quantity < 0 :
				return JsonResponse({'status': 'failure', 'results': 'Insufficient quantity in stock.'}, status=HTTPStatus.BAD_REQUEST)
			Transaction.objects.create(**params)
			Incart.objects.filter(user_id=request.user.uid).delete()
			Users.objects.filter(id=seller_id).update(wallet_amount=Users.objects.get(uid=seller_id).wallet_amount + product.quantity * Product.objects.get(id=product.product_id).price * (1 - Product.objects.get(id=product.product_id).discount))
			Product.objects.filter(id=product.product_id).update(quantity=new_quantity)
			Notification.objects.create(user_id=seller_id, message="You just sold " + str(product.quantity) + " " + Product.objects.get(id=product.product_id).name + ".")
	
		return JsonResponse({'status': 'success', 'results': 'Order placed successfully.'}, status=HTTPStatus.OK)
	else:
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def notifications(request):
	print(request.user.is_authenticated, file=sys.stderr)
	if request.user.is_authenticated:
		uid = request.user.uid
		notifications = Notification.objects.filter(user_id=uid).order_by('-notif_timestamp')
		# print(list(notifications.values()), file=sys.stderr)
		return JsonResponse({'status': 'success', 'results': list(notifications.values())}, status=HTTPStatus.OK)
	else :
		print("Not authenticated", file=sys.stderr)
		return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

	



