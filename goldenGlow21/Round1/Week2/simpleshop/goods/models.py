from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name
