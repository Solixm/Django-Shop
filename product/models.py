from django.db import models


class Storage(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Ram(models.Model):
    title = models.SmallIntegerField()

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    des = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="product")
    storage = models.ManyToManyField(Storage, related_name="products")
    ram = models.ManyToManyField(Ram, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")

    def __str__(self):
        return self.title
