from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from apps.order.models import Order
from apps.product.models import Product


@login_required
def view(request):
    title = 'корзина'
    basket_items = Order.objects.filter(user=request.user).order_by('product__category')
    return render(request, 'order/view.html', {'title': title, 'order_items': basket_items})


@login_required
def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('product:view', args=[product.category.pk, pk]))
    old_item = Order.objects.filter(user=request.user, product=product)
    if old_item:
        old_item[0].quantity += 1
        old_item[0].save()
    else:
        new_item = Order(user=request.user, product=product)
        new_item.quantity += 1
        new_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  
@login_required
def remove(request, pk):
    order_record = get_object_or_404(Order, pk=pk)
    order_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))