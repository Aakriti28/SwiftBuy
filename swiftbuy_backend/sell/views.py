import json
from unicodedata import category
from django.shortcuts import render
from http import HTTPStatus
from django.http import JsonResponse
from user.models import Product, Transaction, Wishlist, Notification, Brand
import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.

def sellinfo(request):
    if request.user.is_authenticated:
        userid = request.user.uid
        products = Product.objects.filter(seller_id=userid)
        return JsonResponse({'status': 'success', 'results': list(products.values())}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def addproduct(request):
    if request.user.is_authenticated:
        info = json.loads(request.body.decode('utf-8').replace("'", '"'))
        params = {
            'category': info['category'],
            'brand': info['brand'],
            'name': info['name'],
            'price': info['price'],
            'quantity_available': info['quantity_available'],
            'discount': info['discount'],
            'product_desc': info['product_desc'],
            'seller': request.user.uid
        }
        brandid = Brand.objects.filter(brand_name=info['brand']).values('brand_id')[0]
        if not brandid:
            Brand.objects.create(brand_name=info['brand'])
            brandid = Brand.objects.filter(brand_name=info['brand']).values('brand_id')[0]
        params['brand'] = brandid
        product = Product.objects.create(**params)
        product = Product.objects.create(category=info['category'], brand=brandid, name=info['name'], price=info['price'], quantity_available=info['quantity_available'], discount=info['discount'], product_desc=info['product_desc'], seller=request.user.uid)
        return JsonResponse({'results': product.product_id, 'status': 'success'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def selling(request):
    if request.user.is_authenticated:
        userid = request.user.uid
        products = Product.objects.filter(seller_id=userid)
        return JsonResponse({'products': list(products.values()), 'status': 'success'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def update(request, productid):
    if request.user.is_authenticated:
        info = json.loads(request.body.decode('utf-8').replace("'", '"'))
        userid = request.user.uid
        prev_quantity = Product.objects.filter(product_id=productid, seller_id=userid).values('quantity_available')[0]['quantity_available']
        if info['quantity_available'] > 0 and prev_quantity == 0:
            wishlist_users = list(Wishlist.objects.filter(product_id=productid).all().values('user_id'))
            Wishlist.objects.filter(product_id=productid).delete()
            for user in wishlist_users:
                Notification.objects.create(user_id=user['user_id'], product_id=productid, message="Your product is now available for purchase.", seen=0, timestamp=datetime.now())
            
        params = {
            'product_id': productid,
            'category': info['category'],
            'brand': info['brand'],
            'name': info['name'],
            'price': info['price'],
            'quantity_available': info['quantity_available'],
            'discount': info['discount'],
            'product_desc': info['product_desc']
        }
        Product.objects.filter(product_id=productid).update(**params)
        return JsonResponse({'status': 'success', 'results': 'Product updated'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def delete(request, productid):
    if request.user.is_authenticated:
        userid = request.user.uid
        Product.objects.filter(product_id=productid, seller_id=userid).delete()
        return JsonResponse({'status': 'success', 'results': 'Product deleted'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def history(request):
    if request.user.is_authenticated:
        userid = request.user.uid
        transactions = Transaction.objects.filter(seller_id=userid)
        products = Product.objects.filter(id__in=list(transactions.values('product_id')))
        return JsonResponse({'transactions': list(transactions.values()), 'products': list(products.values()), 'status': 'success'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def analytics(request):
    if request.user.is_authenticated:
        userid = request.user.uid
        orders = list(Transaction.objects.filter(seller_id=userid).values('order_id'))
        past_week = Transaction.objects.filter(seller_id=userid, order_id__in=orders, orders__trasaction_time__gte=datetime.now() - timedelta(days=7))
        past_month = Transaction.objects.filter(seller_id=userid, order_id__in=orders, orders__trasaction_time__gte=datetime.now() - timedelta(days=30))
        past_year = Transaction.objects.filter(seller_id=userid, order_id__in=orders, orders__trasaction_time__gte=datetime.now() - timedelta(days=365))
        return JsonResponse({'status': 'success', 'past_week': list(past_week.values()), 'past_month': list(past_month.values()), 'past_year': list(past_year.values())}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)
