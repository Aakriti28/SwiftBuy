from itertools import product
from django.shortcuts import render
from django.http import JsonResponse
from user.models import Category, Product
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def categories(request):
    categories = Category.objects.all()
    return JsonResponse({'results': categories})

@login_required
def products(request, categoryid):
    products = Product.objects.filter(category=categoryid)
    return JsonResponse({'results': products})

@login_required  
def viewproduct(request, productid):
    product = Product.objects.get(id=productid)
    return JsonResponse({'results': product})

@login_required
def search(request):
    query = request.GET.get('query')
    products = Product.objects.all().raw('SELECT name, price, discount FROM product natural join brand WHERE name LIKE %s OR description LIKE %s OR brand.name LIKE %s LIMIT 5;', ['%'+query+'%', '%'+query+'%', '%'+query+'%'])
    return JsonResponse({'results': products})