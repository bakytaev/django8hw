from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name} - {self.address}'


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price}'
