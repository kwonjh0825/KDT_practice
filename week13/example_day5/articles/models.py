from django.db import models

# Create your models here.

class Articles(models.Model):
    # 필드 이름 / 데이터 타입 / 제약조건
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)