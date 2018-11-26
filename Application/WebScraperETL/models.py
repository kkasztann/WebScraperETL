from django.db import models

class Opinion(models.Model):
    username = models.CharField(max_length=50)
    productRating = models.CharField(max_length=10)
    productReview = models.TextField()

    def __str__(self):
        return self.username