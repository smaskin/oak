from apps.order.models import Order

def widget(request):
    return {'order': request.user.order_set.all() if request.user.is_authenticated else []}