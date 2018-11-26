from django.db import models

class Opinion(models.Model):
    username = models.CharField(max_length=50)
    productRating = models.CharField(max_length=10)
    productReview = models.TextField()

    def __str__(self):
        return self.username

class ProductID(models.Model):
    productID = models.CharField(max_length=50)

    def __str__(self):
        return self.productID