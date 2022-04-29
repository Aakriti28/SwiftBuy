from django.shortcuts import render
from http import HTTPStatus
from django.http import JsonResponse
from user.models import Product, Transaction, Wishlist, Notification
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
        params = {
            'category': request.POST['category'],
            'brand': request.POST['brand'],
            'name': request.POST['name'],
            'price': request.POST['price'],
            'quantity_available': request.POST['quantity_available'],
            'discount': request.POST['discount'],
            'product_desc': request.POST['product_desc'],
            'seller': request.user
        }
        product = Product.objects.create(**params)
        return JsonResponse({'results': product.product_id, 'status': 'success'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def update(request, productid):
    if request.user.is_authenticated:
        userid = request.user.uid
        prev_quantity = Product.objects.get(product_id=productid, seller_id=userid).quantity_available
        if request.POST['quantity_available'] > 0 and prev_quantity == 0:
            wishlist_users = Wishlist.objects.filter(product_id=productid)
            Wishlist.objects.filter(product_id=productid).delete()
            for user in wishlist_users:
                Notification.objects.create(user=user, product_id=productid, message="Your product is now available for purchase.")
            
        params = {
            'product_id': productid,
            'category': request.POST['category'],
            'brand': request.POST['brand'],
            'name': request.POST['name'],
            'price': request.POST['price'],
            'quantity_available': request.POST['quantity_available'],
            'discount': request.POST['discount'],
            'product_desc': request.POST['product_desc']
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
        transactions = Transaction.objects.filter(seller=userid)
        products = Product.objects.filter(id__in=list(transactions.values('product_id')))
        return JsonResponse({'transactions': list(transactions.values()), 'products': list(products.values()), 'status': 'success'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def analytics(request):
    if request.user.is_authenticated:
        userid = request.user.uid
        orders = Transaction.objects.filter(seller=userid)
        past_week = Transaction.objects.filter(seller=userid, order_id=orders.id, orders__timestamp__gte=datetime.now() - timedelta(days=7))
        past_month = Transaction.objects.filter(seller=userid, order_id=orders.id, orders__timestamp__gte=datetime.now() - timedelta(days=30))
        past_year = Transaction.objects.filter(seller=userid, order_id=orders.id, orders__timestamp__gte=datetime.now() - timedelta(days=365))
        return JsonResponse({'status': 'success', 'past_week': past_week, 'past_month': past_month, 'past_year': past_year}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)
