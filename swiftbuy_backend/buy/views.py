from http import HTTPStatus
from django.shortcuts import render
from user.models import Orders, Transaction, Review
from django.http import JsonResponse
from .forms import AddReviewForm

# Create your views here.

def history(request):
    if request.user.is_authenticated:
        userid = request.user.uid
        results = Transaction.objects.all().raw('SELECT * FROM Orders natural join (SELECT * FROM Transaction WHERE buyer_id = %s group by order_id) as S group by order.order_id, order.timestamp ORDER BY timestamp DESC', [userid])
        return JsonResponse({'status': 'success', 'results': list(results.values())}, status=HTTPStatus.OK)
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

