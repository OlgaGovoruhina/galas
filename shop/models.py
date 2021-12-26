from django.db import models


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


# Модель товара
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


# Модель картинки товара
class ProductImage(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинки товара'

    def __str__(self):
        return f'Картинка товара - {self.product}'
