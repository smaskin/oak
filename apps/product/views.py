from django.shortcuts import render
from .models import Category, Product


def index(request, category = None):
    return render(request, 'product/index.html', {'title': 'Каталог', 'products': Product.objects.all()})


def view(request, category, id):
    return render(request, 'product/view.html', {'product': Product.objects.get(pk=id)})
