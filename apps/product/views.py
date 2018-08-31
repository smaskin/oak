from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from apps.order.models import Order


def index(request, category=0):
    order = []
    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user)

    return render(request, 'product/index.html', {
        'title': 'Каталог',
        'category': int(category),
        'products': Product.objects.filter(category__pk=category) if int(category) > 0 else Product.objects.all(),
        'categories': Category.objects.all(),
        'order': order
    })


def view(request, category, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product/view.html', {'title': product.name, 'product': product})
