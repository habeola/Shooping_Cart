
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Offer, Item


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


def new(request):
    produ = list(Item.objects.get(id=1).products.all())
    return render(request, 'products/new.html', {'produ': produ})


