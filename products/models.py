# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MainCategory(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False, help_text="Bu alan boş bırakılamaz.")
    image = models.ImageField(upload_to='urunresimleri/%Y/%m/%d', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, help_text=u"Link, otomatik alinir, değiştirmeyiniz!!")
    enable = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.title)

class SubCategory(models.Model):

    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="main_category")
    title = models.CharField(max_length=255, null=False, blank=False, help_text="Bu alan boş bırakılamaz.")
    image = models.ImageField(upload_to='urunresimleri/%Y/%m/%d', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=80, null=True, help_text=u"Link, otomatik alinir, değiştirmeyiniz!!")
    enable = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.title)

class Products(models.Model):

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="sub_category")
    title = models.CharField(max_length=255, null = False, blank = False, help_text="Bu alan boş bırakılamaz.")
    price = models.CharField(max_length=255,null=False, blank=False, help_text="Bu alan boş bırakılmaz.")
    image =  models.ImageField(upload_to='urunresimleri/%Y/%m/%d')
    create_date = models.DateTimeField(auto_now_add= True)
    update_date = models.DateTimeField(auto_now= True)
    definition = models.TextField(null=True, help_text="Ürün aciklamasini giriniz.")
    slug = models.SlugField(max_length=80, null=True, help_text=u"Link, otomatik alinir, değiştirmeyiniz!!")
    viewCount = models.IntegerField(default=0)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.title)


