from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbol
class post(models.Model):
    title=models.CharField(max_length=50,unique=True,error_messages={'unique':'제목은 겹칠 수 없습니다 !'})
    content=models.TextField(validators=[MinLengthValidator(10,"글은 10자 이상 적어주세요"),validate_symbol])
    dt_created=models.DateTimeField(verbose_name="Date Created",auto_now_add=True)
    dt_modified=models.DateTimeField(verbose_name="Date Modified",auto_now=True)
    
    def __str__(self):
        return self.title

# Create your models here.
