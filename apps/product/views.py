from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete
from apps.order.models import Position
from .models import Category, Product


def index(request, category=0):
    category = int(category)
    query = Product.objects.select_related()
    return render(request, 'product/index.html', {
        'title': 'Каталог',
        'category': category,
        'products': cache.get_or_set('prods_with_cat_{}'.format(category), query.filter(category__pk=category) if category > 0 else query.all()),
        'categories': cache.get_or_set('cats', Category.objects.all())
    })


def view(request, category, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product/view.html', {'title': product.name, 'product': product})


@receiver(pre_save, sender=Position)
def decrease_quantity_by_position_update(sender, update_fields, instance, **kwargs):
    if update_fields is 'quantity' or 'product':
        instance.product.quantity -= instance.quantity - (sender.get_item(instance.pk).quantity if instance.pk else 0)
        instance.product.save()


@receiver(pre_delete, sender=Position)
def increase_quantity_by_position_delete(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()
