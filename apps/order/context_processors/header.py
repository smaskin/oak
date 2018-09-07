from apps.order.models import Order

def widget(request):
    return {'order': Order.objects.filter(user=request.user) if request.user.is_authenticated else []}