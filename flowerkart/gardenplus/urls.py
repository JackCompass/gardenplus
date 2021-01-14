from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('about', views.about, name = 'about'),
	path('contact', views.contact, name = 'contact'),
	path('products', views.products, name = 'products'),
	path('<int:product_id>', views.details, name = 'details'),
	path('cart', views.cart, name = 'cart'),
]