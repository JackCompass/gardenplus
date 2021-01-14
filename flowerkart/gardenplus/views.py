from django.shortcuts import render, get_object_or_404
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

def details(request, product_id):
	item = get_object_or_404(Products, pk = product_id)
	print(item.name)
	print(item.price)
	return render(request, 'gardenplus/product_detail.html', {
			'item' : item,
		})

def cart(request):
	pass