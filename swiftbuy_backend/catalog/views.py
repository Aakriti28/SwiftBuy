from itertools import product
from django.shortcuts import render
from django.http import JsonResponse
from user.models import Category, Product

# Create your views here.

def categories(request):
    categories = Category.objects.all()
    return JsonResponse({'results': categories})

def products(request, categoryid):
    products = Product.objects.filter(category=categoryid)
    return JsonResponse({'results': products})
    
def viewproduct(request, productid):
    product = Product.objects.get(id=productid)
    return JsonResponse({'results': product})

def search(request):
    query = request.GET.get('query')
    products = Product.objects.all().raw('SELECT name, price, discount FROM product natural join brand WHERE name LIKE %s OR description LIKE %s OR brand.name LIKE %s LIMIT 5;', ['%'+query+'%', '%'+query+'%', '%'+query+'%'])
    return JsonResponse({'results': products})