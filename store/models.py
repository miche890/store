from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.product.name + ' - ' + str(self.quantity)
