from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

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

    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='followers')

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

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    dt_created = models.DateTimeField(auto_now_add=True)

    dt_updated = models.DateTimeField(auto_now=True)

    is_sold = models.BooleanField(default=False)

    likes = GenericRelation('Like', related_query_name='post')

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-dt_created']


class Comment(models.Model):
    content = models.TextField(max_length=500, blank=False)

    dt_created = models.DateTimeField(auto_now_add=True)

    dt_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    likes = GenericRelation('Like', related_query_name='comment')

    def __str__(self):
        return self.content[:30]

    class Meta:
        ordering = ['dt_created']


class Like(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    liked_object = GenericForeignKey()

    def __str__(self):
        return f"({self.user}, {self.liked_object})"