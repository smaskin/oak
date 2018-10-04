from django.db import models
from django.conf import settings
from django.utils.functional import cached_property
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
    status = models.CharField(db_index=True, verbose_name='статус', max_length=3, choices=ORDER_STATUS_CHOICES, default=CART)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    @cached_property
    def total_text(self):
        positions = self.positions.select_related().all()
        if not positions:
            return 'Пусто'
        total_quantity = sum(list(map(lambda x: x.quantity, positions)))
        total_cost = sum(list(map(lambda x: x.cost, positions)))
        product = positions[0].product
        return "{} {}, {} {}".format(total_quantity, product.unit, total_cost, product.currency)
