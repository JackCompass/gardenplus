from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'gardenplus/index.html')

def about(request):
	return render(request, 'gardenplus/about.html')

def contact(request):
	return render(request, 'gardenplus/contact.html')

def products(request):
	return render(request, 'gardenplus/products.html')