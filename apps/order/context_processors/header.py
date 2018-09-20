from apps.order.models import Order

def widget(request):
    return {'order': request.user.order_set.filter(status=Order.CART).first() if request.user.is_authenticated else []}