from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    KINDS = (
        ('R','Ресторан'),
        ('C','Кафе'),
        ('H','Отель'),
        ('M','Магазин'),
        ('R','Торговая Фирма'),
        ('X','Предприниматель'),
        (None,'Неустановленный тип предприятия'),
    )
    title = models.CharField(max_length=70,verbose_name='Наименование')
    adress = models.CharField(max_length=100, verbose_name='Адрес')
    id_int = models.CharField(max_length=70, verbose_name='ID организации')
    kind = models.CharField(max_length=1,choices=KINDS,)

class Item(models.Model):

