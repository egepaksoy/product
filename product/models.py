from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Ürün Başlık')
    info = models.TextField(max_length=1000, verbose_name='Ürün Açıklama')
    price = models.CharField(max_length=6, verbose_name='Ürün Fiyatı')

    def __str__(self):
        return self.title
