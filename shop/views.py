from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product

# Create your views here.
def home(request):
	context = {
		'products': Product.objects.filter(is_active=True)
	}
	return render(request, 'shop/index.html', context)

def detail(request, slug):
	context = {
		'product': get_object_or_404(Product, slug=slug, is_active=True),
	}
	return render(request, 'shop/detail.html', context)