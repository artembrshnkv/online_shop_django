from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=255)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)

    def get_absolute_url(self):
        return reverse('all_subcategories', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.slug}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    title = models.CharField(verbose_name='Подкатегория', max_length=255)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)
    category = models.ForeignKey(verbose_name='Категория', to=Category, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('goods_by_subcategory', kwargs={'category': self.category,
                                                       'slug': self.slug})

    def __str__(self):
        return f'{self.slug}'

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


    def get_absolute_url(self):
        return reverse('show_product', kwargs={'category': self.category,
                                               'subcategory': self.subcategory,
                                               'pk': self.pk})

    def __str__(self):
        return f'{self.slug}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Comment(models.Model):
    stars = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    username = models.ForeignKey(verbose_name='Автор', to=User, on_delete=models.PROTECT)
    content = models.TextField(verbose_name='Комментарий')
    product = models.ForeignKey(verbose_name='Id товара', to=Goods, on_delete=models.PROTECT)
    rating = models.IntegerField(verbose_name='Оценка', choices=stars, default=5)
    time_creation = models.TimeField(verbose_name='Дата создания', auto_now_add=True)
    time_update = models.TimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.username}_{self.product}'

    def get_absolute_url(self):
        return reverse('add_comment', kwargs={'pk': self.pk,
                                              'category': Goods.objects.get(pk=self.product.category)[0],
                                              'subcategory': Goods.objects.get(pk=self.product.subcategory)[0]})

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    product = models.ForeignKey(to=Goods, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user}_{self.product}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
