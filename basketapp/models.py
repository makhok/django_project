from django.db import models
from django.conf import settings
from mainapp.models import Product

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return f'{self.product.name}, {self.quantity}'

    @property
    def quantity_product(self):
        items = Basket.objects.filter(user=self.user)
        quantity = sum(list(map(lambda x: x.quantity, items)))
        return quantity

    @property
    def coast_product(self):
        items = Basket.objects.filter(user=self.user)
        all_coast = sum(list(map(lambda x: x.product.price * x.quantity, items)))
        return all_coast


