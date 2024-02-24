from django.db import models

# Create your models here.


class Order(models.Model):
    oid = models.IntegerField()
    product = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.FloatField()
    del_date = models.DateField()
    add = models.CharField(max_length=50)
