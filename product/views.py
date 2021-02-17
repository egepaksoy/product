from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product

# Create your views here.


def home(req):
    products = Product.objects.all()
    return render(req, 'index.html', {"products": products})


def product(req, id):
    product = get_object_or_404(Product, id=id)

    return render(req, 'product.html', {"product": product})
