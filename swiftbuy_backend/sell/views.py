from django.shortcuts import render
from django.http import JsonResponse
from user.models import Product, Transaction
import datetime
from datetime import timedelta

# Create your views here.

def sellinfo(request, userid):
    products = Product.objects.filter(seller=request.user)
    return JsonResponse({'products': products})

def update(request, userid, productid):
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

def history(request, userid):
    transactions = Transaction.objects.filter(seller=userid)
    products = Product.objects.filter(id=transactions.product_id)
    return JsonResponse({'transactions': transactions, 'products': products})

def analytics(request, userid):
    orders = Transaction.objects.filter(seller=userid)
    past_week = Transaction.objects.filter(seller=userid, order_id=orders.id, orders__timestamp__gte=datetime.now() - timedelta(days=7))
    past_month = Transaction.objects.filter(seller=userid, order_id=orders.id, orders__timestamp__gte=datetime.now() - timedelta(days=30))
    past_year = Transaction.objects.filter(seller=userid, order_id=orders.id, orders__timestamp__gte=datetime.now() - timedelta(days=365))
    return JsonResponse({'past_week': past_week, 'past_month': past_month, 'past_year': past_year})

