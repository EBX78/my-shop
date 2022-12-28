from django.urls import path
from .views import *

app_name = 'shop'
urlpatterns = [
	path("", all_products, name='all_products'),
	path('product/<slug:slug>', detail, name='detail')
]