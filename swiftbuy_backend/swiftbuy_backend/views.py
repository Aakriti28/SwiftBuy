from django.shortcuts import render, redirect
from django.http import JsonResponse


# Create your views here.
def homepage(request):
	# return render(request, 'home.html')
	return JsonResponse({'data': 'Hello'})


