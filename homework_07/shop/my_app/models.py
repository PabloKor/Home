from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

