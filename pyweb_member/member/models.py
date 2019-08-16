from django.db import models
from django.contrib.auth.models import User
from django import forms


# Django에 미리 만들어진 ModelForm 클래스 상속
# 탬플릿에서 form을 직접 만들지 않고 미리 만들어진 form을 사용할 수 있음
class UserForm(forms.ModelForm):
    class Meta: # 클래스를 만드는 클래스
        model = User # 사용자 정보를 관리하는 내장 클래스
        fields = ['username', 'email', 'password']