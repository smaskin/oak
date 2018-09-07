from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Product


def index(request, category=0):
    return render(request, 'product/index.html', {
        'title': 'Каталог',
        'category': int(category),
        'products': Product.objects.filter(category__pk=category) if int(category) > 0 else Product.objects.all(),
        'categories': Category.objects.all(),
    })


def view(request, category, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product/view.html', {'title': product.name, 'product': product})
