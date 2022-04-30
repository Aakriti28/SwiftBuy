from http import HTTPStatus
from django.shortcuts import render
from user.models import Orders, Transaction, Review, Product
from django.http import JsonResponse
from .forms import AddReviewForm

# Create your views here.

def history(request):
    if request.user.is_authenticated:
        userid = request.user.uid
        quantities = list(Transaction.objects.filter(buyer_id=userid).values_list('product_id', 'quantity').order_by('product_id'))
        product_ids = [x[0] for x in quantities]
        products = list(Product.objects.filter(product_id__in=product_ids).values().order_by('product_id'))
        for i in range(len(quantities)) :
            products[i]['quantity'] = quantities[i][1]
        return JsonResponse({'status': 'success', 'results': products}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

def addreview(request, productid):
    if request.user.is_authenticated:
        form = AddReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            params = {
                'product_id': productid,
                'user_id': request.user.uid,
                'review': review.review,
                'rating': review.rating
            }
            Review.objects.create(**params)
            return JsonResponse({'status': 'success', 'results': 'Product Review added successfully.'}, status=HTTPStatus.OK)
        else:
            return JsonResponse({'status': 'failure', 'results': 'Product Review not added.'}, status=HTTPStatus.BAD_REQUEST)
    else:
        return JsonResponse({'status': 'auth_failure', 'results': 'User not authenticated'}, status=HTTPStatus.UNAUTHORIZED)

