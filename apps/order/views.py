from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.order.models import Order, Position
from apps.product.models import Product


@login_required
def index(request):
    title = 'заказы'
    return render(request, 'order/index.html', {'title': title, 'models': Order.objects.filter(user=request.user, status=Order.FORMING)})


@login_required
def view(request):
    title = 'корзина'
    order = Order.objects.filter(user=request.user, status=Order.CART).first()
    return render(request, 'order/view.html', {'title': title, 'order': order})


@login_required
def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('product:view', args=[product.category.pk, pk]))
    order = Order.objects.filter(user=request.user, status=Order.CART).first()
    if not order:
        order = Order(user=request.user)
        order.save()
    current = order.positions.filter(product=product)
    if current:
        current[0].quantity += 1
        current[0].save()
    else:
        position = Position(product=product)
        position.quantity = 1
        position.save()
        order.positions.add(position)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, pk):
    order = Order.objects.get(user=request.user, status=Order.CART)
    position = get_object_or_404(Position, pk=pk)
    position.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) if order.positions.exists() else HttpResponseRedirect(reverse('product:index'))


@login_required
def pay(request):
    order = Order.objects.get(user=request.user, status=Order.CART)
    order.status = Order.FORMING
    order.save()
    messages.add_message(request, messages.INFO, 'Поздравляем заказ успешно сформирован!')
    return HttpResponseRedirect(reverse('product:index'))
