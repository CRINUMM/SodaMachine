from tabnanny import verbose
from unicodedata import name
from django.db import models


class Soda(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta():
        verbose_name = 'Soda'
        verbose_name_plural = 'Soda'
        ordering = ('id', 'name')


class Transactions(models.Model):
    money = models.DecimalField(max_digits=6, decimal_places=2)
    change = models.DecimalField(max_digits=6, decimal_places=2)
    date_add = models.DateTimeField(auto_now_add=True)
    soda_id = models.ForeignKey(Soda, on_delete = models.CASCADE)

    class Meta():
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ('id', 'date_add')
