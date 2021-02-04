from django.db import models

# Create your models here.
# class Board(models.Model):
#     # id컬럼 자동추가, 기본키, 자동증가
#     title = models.CharField(max_length=10)
#     username = models.CharField(max_length=10)
#     pw = models.CharField(max_length=10)
#     # 저장 시점에 시간 자동등록
#     regdate = models.DateTimeField(auto_now_add=True)