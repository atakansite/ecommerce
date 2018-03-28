# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Products

# Create your models here.
class User(AbstractUser):

    adress = models.CharField(max_length=255, null= True, blank= True)
    telephone =   models.CharField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.title)