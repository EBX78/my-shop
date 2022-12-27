from django.db import models
from django.contrib.auth.models import User
from extentions.utils import jalali_converter, farsi_format_price

class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True, verbose_name='عنوان')
    slug = models.SlugField(max_length=256, unique=True, verbose_name='آدرس')
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural='دسته بندی ها'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, verbose_name='دسته بندی')
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE, verbose_name='تولید شده توسط')
    title = models.CharField(max_length=256, verbose_name='عنوان')
    author = models.CharField(max_length=256, verbose_name='نویسنده')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/', verbose_name='عکس')
    slug = models.SlugField(max_length=256, unique=True, verbose_name='آدرس')
    # price = models.DecimalField(decimal_places=3, max_digits=8, verbose_name='قیمت')
    price = models.IntegerField(verbose_name='قیمت')
    in_stock = models.BooleanField(default=True, verbose_name='موجود در انبار')
    is_active = models.BooleanField(default=True, verbose_name='نمایش دادن')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ افزودن')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین دستکاری')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['-in_stock', '-updated']

    def __str__(self):
        return self.title

    def fcreated(self):
        return jalali_converter(self.created)
    fcreated.short_description = "تاریخ افزودن"

    def fupdated(self):
        return jalali_converter(self.updated)
    fupdated.short_description = "آخرین دستکاری"

    def fprice(self):
        return farsi_format_price(self.price)
    fprice.short_description = "قیمت"