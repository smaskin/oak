from django.shortcuts import render
from .models import Category, Product


def index(request):
    products = [
        {'href': 'detail', 'name': 'Дуб', 'img': 'images/oak.jpeg'},
        {'href': 'detail', 'name': 'Липа', 'img': 'images/linden.jpeg'},
        {'href': 'detail', 'name': 'Клен', 'img': 'images/maple.jpeg'},
    ];
    products = Product.objects.all()
    return render(request, 'product/index.html', {'title': 'Каталог', 'products': products})


def view(request):
    return render(request, 'product/view.html', {'title': 'Каталог'})
