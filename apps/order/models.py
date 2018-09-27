from django.db import models
from django.conf import settings
from apps.product.models import Product


class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @staticmethod
    def get_item(pk):
        return Position.objects.get(pk=pk)

    @property
    def cost(self):
        return self.product.price * self.quantity

    @property
    def cost_text(self):
        return "{} {}".format(self.cost, self.product.currency)


class Order(models.Model):
    CART = 'CT'
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (CART, 'корзина'),
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачен'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    positions = models.ManyToManyField(Position)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name='статус', max_length=3, choices=ORDER_STATUS_CHOICES, default=CART)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    @property
    def total_text(self):
        position = self.positions.first()
        if not position:
            return 'Пусто'
        product = position.product
        return "{} {}, {} {}".format(self.total_quantity, product.unit, self.total_cost, product.currency)

    @property
    def total_quantity(self):
        _items = self.positions.all()
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    @property
    def total_cost(self):
        _items = self.positions.all()
        _totalcost = sum(list(map(lambda x: x.cost, _items)))
        return _totalcost
