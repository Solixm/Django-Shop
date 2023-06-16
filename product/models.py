from django.db import models


class Storage(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Ram(models.Model):
    title = models.IntegerField()

    def __str__(self):
        return str(self.title)


class Color(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    des = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="product")
    storage = models.ManyToManyField(Storage, related_name="products")
    ram = models.ManyToManyField(Ram, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='informations')
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text[:30]
