from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from apps.order.models import Order
from apps.product.models import Product


def view(request):
    return render(request, 'order/view.html', {})


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    old_item = Order.objects.filter(user=request.user, product=product)
    if old_item:
        old_item[0].quantity += 1
        old_item[0].save()
    else:
        new_item = Order(user=request.user, product=product)
        new_item.quantity += 1
        new_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request):
    return render(request, 'order/view.html', {})
