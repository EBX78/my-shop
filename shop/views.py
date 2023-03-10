from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product

def categories(request):
	return {'categories': Category.objects.all()}

def all_products(request):
	products = Product.objects.filter(is_active=True).order_by('-in_stock', '-updated')
	return render(request, 'shop/index.html', {'products':products})

def detail(request, slug):
	product = get_object_or_404(Product, slug=slug, is_active=True)
	return render(request, 'shop/detail.html', {'product':product})