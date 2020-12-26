from django.shortcuts import render
from .models import Products
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'gardenplus/index.html')

def about(request):
	return render(request, 'gardenplus/about.html')

def contact(request):
	return render(request, 'gardenplus/contact.html')

def products(request):
	product = Products.objects.all()
	return render(request, 'gardenplus/products.html',{
			'product' : product,
		})