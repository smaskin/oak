from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponseForbidden, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.order.models import Order, Position
from apps.product.models import Product


@login_required
def index(request):
    title = 'заказы'
    return render(request, 'order/index.html', {'title': title, 'models': Order.objects.filter(user=request.user, status=Order.FORMING, positions__isnull=False)})


@login_required
def view(request):
    title = 'корзина'
    order = Order.objects.filter(user=request.user, status=Order.CART).first()
    return render(request, 'order/view.html', {'title': title, 'order': order})


@login_required
def edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        position = get_object_or_404(Position, pk=pk)
        order = Order.objects.filter(pk=position.order_set.first().pk, user=request.user).first()
        if not order:
            return HttpResponseForbidden()

        if quantity > 0:
            position.quantity = quantity
            position.save()
        else:
            position.delete()
        return JsonResponse({'result': render_to_string('order/_positions.html', {'order': order})})
    else:
        return HttpResponseForbidden()


@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, status=Order.CART).first()
    return JsonResponse({'result': render_to_string('order/_cart.html', {'order': order})})


@login_required
def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    referer = request.META.get('HTTP_REFERER')
    redirect = HttpResponseRedirect(reverse('product:view', args=[product.category.pk, pk]))
    if referer and 'login' in referer:
        return redirect
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
    return HttpResponseRedirect(referer) if referer else redirect


@login_required
def remove(request, pk):
    if request.is_ajax():
        position = get_object_or_404(Position, pk=pk)
        order = position.order_set.first()
        if order.user.pk != request.user.pk:
            return HttpResponseForbidden()
        position.delete()
        return JsonResponse({'result': render_to_string('order/_positions.html', {'order': order})})
    else:
        return HttpResponseForbidden()


@login_required
def pay(request):
    order = Order.objects.get(user=request.user, status=Order.CART)
    order.status = Order.FORMING
    order.save()
    messages.add_message(request, messages.INFO, 'Поздравляем заказ успешно сформирован!')
    return HttpResponseRedirect(reverse('product:index'))
