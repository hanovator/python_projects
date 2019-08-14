from django.db import models
# 날짜 자료형 처리를 위하여 로딩
from datetime import datetime


class Memo(models.Model): # django의 model 클래스를 상속받음
    idx = models.AutoField(primary_key=True) # 자동증가
    writer = models.TextField(null=False)
    memo = models.TextField(null=False)
    # 기본값을 시스템의 현재시간으로 설정
    post_date = models.DateTimeField(default=datetime.now, blank=True)
