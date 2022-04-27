from django.shortcuts import render
from user.models import Orders, Transaction, Review
from django.http import JsonResponse
from .forms import AddReviewForm

# Create your views here.

def history(request, userid):
    results = Transaction.objects.all().raw('SELECT * FROM Orders natural join (SELECT * FROM Transaction WHERE buyer_id = %s group by order_id) as S group by order.order_id, order.timestamp ORDER BY timestamp DESC', [userid])
    return JsonResponse({'results': results})

def addreview(request, productid):
    form = AddReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        params = {
            'product_id': productid,
            'user_id': request.user.id,
            'review': review.review,
            'rating': review.rating
        }
        Review.objects.create(**params)
        return JsonResponse({'status': 'Product Review added successfully.'})
    else:
        return JsonResponse({'status': 'Product Review not added.'})

