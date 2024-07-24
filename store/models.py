from cloudinary.models import CloudinaryField
from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

import datetime

# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, verbose_name='Descripción')
    highlight = models.BooleanField(default=False, verbose_name='Destacar')
    image = CloudinaryField(resource_type='image', null=True, blank=True, verbose_name='Imagen', default='')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[str(self.slug)])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    slug = models.SlugField(max_length=100)
    image = CloudinaryField(resource_type='image', verbose_name='Imagen', default='')
    description = models.TextField(max_length=500, verbose_name='Descripción')
    price = models.PositiveIntegerField(verbose_name='Precio')
    available = models.BooleanField(default=True, verbose_name='Disponibilidad')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id), self.slug])


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.product.name + ' - ' + str(self.quantity)
