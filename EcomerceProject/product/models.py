from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS = (
        ('Pending', 'PENDING'),
        ('Published', 'PUBLISHED'),
        ('Stock Out', 'STOCK OUT')
    )
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    Description = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')

    def __str__(self):
        return self.name
