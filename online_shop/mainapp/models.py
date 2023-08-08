from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=255)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    title = models.CharField(verbose_name='Подкатегория', max_length=255)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)
    category = models.ForeignKey(verbose_name='Категория', to=Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Goods(models.Model):
    category = models.ForeignKey(verbose_name='Категория', to=Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(verbose_name='Подкатегория', to=Subcategory, on_delete=models.PROTECT)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    price = models.IntegerField(verbose_name='Цена')
    active_offer = models.BooleanField(verbose_name='В продаже', default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Comment(models.Model):
    username = models.ForeignKey(verbose_name='Автор', to=User, on_delete=models.PROTECT)
    content = models.TextField(verbose_name='Комментарий')
    time_creation = models.TimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update = models.TimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
