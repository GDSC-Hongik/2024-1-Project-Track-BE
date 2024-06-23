from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from .validators import validate_no_special_characters


class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
    )

    kakao_id = models.CharField(
        max_length=20,
        null=True,
        validators=[validate_no_special_characters],
    )

    address = models.CharField(
        max_length=40,
        null=True,
        validators=[validate_no_special_characters],
    )

    profile_pic = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.CharField(max_length=60)

    item_price = models.IntegerField(validators=[MinValueValidator(1)])

    CONDITION_CHOICES = [
        ('새제품', '새제품'),
        ('최상', '최상'),
        ('상', '상'),
        ('중', '중'),
        ('하', '하'),
    ]
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default=None)

    item_details = models.TextField(blank=True)

    image1 = models.ImageField(upload_to='item_pics')

    image2 = models.ImageField(upload_to='item_pics', blank=True)

    image3 = models.ImageField(upload_to='item_pics', blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    dt_created = models.DateTimeField(auto_now_add=True)

    dt_updated = models.DateTimeField(auto_now=True)

    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=500, blank=False)

    dt_created = models.DateTimeField(auto_now_add=True)

    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:30]