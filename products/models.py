from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)
    item = models.ForeignKey(
        Item, related_name='products', on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
