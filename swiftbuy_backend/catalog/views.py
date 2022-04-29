from http import HTTPStatus
from django.shortcuts import render
from django.http import JsonResponse
from user.models import Category, Product
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# @csrf_exempt
def categories(request):
    # print(request.user.is_authenticated)
    print("ATLEAST here")
    if request.user.is_authenticated:
        print("NOT SO SAD")
        categories = Category.objects.all()
        return JsonResponse({'status': 'success', 'results': list(categories.values())}, status=HTTPStatus.OK)
    else :
        print("SAD")
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def products(request, categoryid):
    if request.user.is_authenticated:
        products = Product.objects.filter(category_id=categoryid)
        return JsonResponse({'status': 'success', 'results': list(products.values())}, status=HTTPStatus.OK)
    else :
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)
 
def viewproduct(request, productid):
    if request.user.is_authenticated:
        product = Product.objects.get(product_id=productid)
        return JsonResponse({'status': 'success', 'results': product.__dict__}, status=HTTPStatus.OK)
    else :
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def search(request):
    if request.user.is_authenticated:
        query = request.GET['query']
        # products = Product.objects.filter(name__icontains=query)
        products = Product.objects.all().raw('SELECT name, price, discount FROM product natural join brand WHERE name LIKE %s OR description LIKE %s OR brand.name LIKE %s LIMIT 5;', ['%'+query+'%', '%'+query+'%', '%'+query+'%'])
        return JsonResponse({'status': 'success', 'results': list(products.values())}, status=HTTPStatus.OK)
    else :
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)