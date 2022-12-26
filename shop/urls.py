from django.urls import path
from .views import *

app_name = 'shop'
urlpatterns = [
	path("", home, name='home'),
	path('product/<slug:slug>', detail, name='detail')
]