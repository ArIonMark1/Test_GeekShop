from django.conf import settings
from django.db import models

# Create your models here.
from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    DELIVERY = 'DLV'
    DONE = 'DN'
    CANCELED = 'CNC'

    STATUSES = (
        (FORMING, 'формирование'),
        (SENT_TO_PROCEED, 'паредан на обработку'),
        (DELIVERY, 'доставка'),
        (DONE, 'выдан'),
        (CANCELED, 'отменен'),

    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, default=FORMING)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заказ номер {self.pk}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_total_cost(self):
        pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def get_product_cost(self):
        return self.quantity * self.product.price