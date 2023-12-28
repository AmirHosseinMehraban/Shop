from django.db import models
from home.models import Product
from accounts.models import MyUser
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    discount = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.paid}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='porder')
    price = models.FloatField()
    quantity = models.SmallIntegerField()

    def __str__(self):
        return f'{self.order} - {self.product}'
