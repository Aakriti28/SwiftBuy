from django.shortcuts import render
from django.http import JsonResponse
from user.models import Product, Transaction, Wishlist, Notification
import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def sellinfo(request, userid):
    products = Product.objects.filter(seller=request.user)
    return JsonResponse({'products': products})

@login_required
def addproduct(request, userid):
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
    return JsonResponse({'product_id': product.id, 'status': 'Product added successfully.'})

@login_required
def update(request, userid, productid):
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
    return JsonResponse({'status': 'Product updated successfully.'})

@login_required
def delete(request, userid, productid):
    Product.objects.filter(product_id=productid, seller_id=userid).delete()
    return JsonResponse({'status': 'Product deleted successfully.'})

@login_required
def history(request, userid):
    transactions = Transaction.objects.filter(seller=userid)
    products = Product.objects.filter(id=transactions.product_id)
    return JsonResponse({'transactions': transactions, 'products': products})

@login_required
def analytics(request, userid):
    orders = Transaction.objects.filter(seller=userid)
    past_week = Transaction.objects.filter(seller=userid, order_id=orders.id, orders__timestamp__gte=datetime.now() - timedelta(days=7))
    past_month = Transaction.objects.filter(seller=userid, order_id=orders.id, orders__timestamp__gte=datetime.now() - timedelta(days=30))
    past_year = Transaction.objects.filter(seller=userid, order_id=orders.id, orders__timestamp__gte=datetime.now() - timedelta(days=365))
    return JsonResponse({'past_week': past_week, 'past_month': past_month, 'past_year': past_year})

