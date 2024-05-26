from django.db import models

# Create your models here.

class menu(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    price=models.IntegerField()
    img_source=models.CharField(max_length=260)
    
    def __str__(self) :
        return self.name
    
