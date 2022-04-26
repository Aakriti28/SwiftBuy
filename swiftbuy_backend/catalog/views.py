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
    products = Product.objects.filter(name__icontains=query).filter(product_desc__icontains=query)
    return JsonResponse({'results': products})