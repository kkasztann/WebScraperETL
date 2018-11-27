from django.db import models

class Opinion(models.Model):
    productID = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    productRating = models.CharField(max_length=10)
    productReview = models.TextField()

    def __str__(self):
        return self.productID + ' | ' + self.username

class Product(models.Model):
    productID = models.CharField(max_length=50)
    productName = models.CharField(max_length=50)
    parameter = models.CharField(max_length=80)
    value = models.CharField(max_length=80)

    def __str__(self):
        return self.productID + ' | ' + self.parameter

class ProductID(models.Model):
    productID = models.CharField(max_length=50)

    def __str__(self):
        return self.productID