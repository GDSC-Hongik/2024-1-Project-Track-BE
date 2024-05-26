from django.db import models

# Create your models here.

class Post(models.Model):
    #글의 제목, 내용, 작성일, 마지막 수정일
    title = models.CharField(max_length=50)
    content = models.TextField() #TextField는 길이 제한 없음
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True) #verbose_name = 별명, 읽기 편한 형태로 알려줌
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title
