from django.shortcuts import render, redirect
from django.http import JsonResponse
from user.models import Users, Product, Transaction, Orders, Addmoney, Incart, Notification, Wishlist
from .forms import AddMoneyForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
	advertised_products = Product.objects.filter(is_advertised=True)
	return JsonResponse({'advertised_products': advertised_products})

@login_required
def about(request):
	if request.method == 'GET':
		details = Users.objects.get(id=request.user.uid)
		return JsonResponse({'results': details})
	elif request.method == 'POST':
		params = {
			'name': request.POST['name'],
			'email': request.POST['email'],
			'phone': request.POST['phone'],
			'address': request.POST['address'],
			'shipping_address': request.POST['shipping_address']
		}
		Users.objects.filter(id=request.user.uid).update(**params)
		return JsonResponse({'status': 'Profile updated successfully.'})

@login_required
def wallet(request):
	transactions = Transaction.objects.all().raw('(SELECT (product.price * (1 - product.discount) * transaction.quantity * -1) AS amount, timestamp, "Bought" AS type FROM transaction NATURAL JOIN product, order WHERE order.id = transaction.order_id AND transaction.buyer_id = %s) UNION (SELECT (product.price * (1 - product.discount) * transaction.quantity) AS amount, timestamp, "Sold" AS type FROM transaction NATURAL JOIN product, order WHERE order.id = transaction.order_id AND transaction.seller_id = %s) UNION (SELECT amount, timestamp, "Added" AS type FROM add_money WHERE user_id = %s) ORDER BY timestamp DESC;', [request.user.uid, request.user.uid, request.user.uid])
	return JsonResponse({'transactions': transactions})

@login_required
def addmoney(request):
	form = AddMoneyForm(request.POST)
	if form.is_valid():
		params = {
			'user_id': request.user.uid,
			'amount': form.cleaned_data['amount'],
			'payment_method': form.cleaned_data['payment_method']
		}
		Addmoney.objects.create(**params)
		Users.objects.filter(uid=request.user.uid).update(wallet_amount=Users.objects.get(uid=request.user.uid).wallet_amount + form.cleaned_data['amount'])
		return JsonResponse({'status': 'Money added successfully.'})
	else :
		return JsonResponse({'status': 'Money not added.'})

@login_required
def cart(request):
	if request.method == 'GET':
		cart_products = Incart.objects.filter(user_id=request.user.uid)
		return JsonResponse({'cart_products': cart_products})
	elif request.method == 'POST':
		params = {
			'user_id': request.user.uid,
			'product_id': request.POST['product_id'],
			'quantity': request.POST['quantity']
		}
		Incart.objects.create(**params)
		return JsonResponse({'status': 'Product added to cart successfully.'})

@login_required
def wishlist(request):
	if request.method == 'GET':
		wishlist_products = Wishlist.objects.filter(user_id=request.user.uid)
		return JsonResponse({'wishlist_products': wishlist_products})
	elif request.method == 'POST':
		params = {
			'user_id': request.user.uid,
			'product_id': request.POST['product_id'],
		}
		Wishlist.objects.create(**params)
		return JsonResponse({'status': 'Product added to wishlist successfully.'})

@login_required
def order(request):
	
	cart_products = Incart.objects.filter(user_id=request.user.uid)
	total_amount = Incart.objects.filter(user_id=request.user.uid).all().raw('SELECT SUM(product.price * (1 - product.discount) * quantity) AS total_amount FROM incart NATURAL JOIN product WHERE user_id = %s', [request.user.uid])
	new_balance = Users.objects.get(uid=request.user.uid).wallet_amount - total_amount[0].total_amount
	payment_id = request.GET['payment_id']
	if payment_id == 4 :
		if new_balance < 0 :
			return JsonResponse({'status': 'Insufficient balance in wallet, please choose a different payment method or add money to your wallet.'})
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
			return JsonResponse({'status': 'Insufficient quantity of product.'})
		Transaction.objects.create(**params)
		Incart.objects.filter(user_id=request.user.uid).delete()
		Users.objects.filter(id=seller_id).update(wallet_amount=Users.objects.get(uid=seller_id).wallet_amount + product.quantity * Product.objects.get(id=product.product_id).price * (1 - Product.objects.get(id=product.product_id).discount))
		Product.objects.filter(id=product.product_id).update(quantity=new_quantity)
		Notification.objects.create(user_id=seller_id, message="You just sold " + str(product.quantity) + " " + Product.objects.get(id=product.product_id).name + ".")
	
	return JsonResponse({'status': 'Order placed successfully.'})

@login_required
def notifications(request):
	notifications = Notification.objects.filter(user_id=request.user.uid).order_by('-timestamp')
	return JsonResponse({'notifications': notifications})

	



