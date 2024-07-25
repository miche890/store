from django.db import models
from store.models import Product


# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Nombre(s)")
    last_name = models.CharField(max_length=50, verbose_name="Apellido(s)")
    email = models.EmailField(verbose_name="Correo Electrónico")
    address = models.CharField(max_length=250, verbose_name='Dirección')
    postal_code = models.CharField(max_length=20, verbose_name="Código postal")
    city = models.CharField(max_length=100, verbose_name='Ciudad')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    paid = models.BooleanField(default=False, verbose_name="Pagado")

    class Meta:
        ordering = ['-created']
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Orden {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Orden')
    product = models.ForeignKey(Product, related_name='order_item', on_delete=models.CASCADE, verbose_name='Producto')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Precio')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Cantidad')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
