from django.db import models


# Django에서 제공하는 Model 클래스를 상속받음
# 모델클레스는 실제 테이블과 매핑됨
class Bookmark(models.Model):
    # 테이블의 필드와 매핑되는 변수들
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField("url", unique=True)

    # 객체를 문자열로 표현하는 함수
    def __str__(self):
        return self.title
