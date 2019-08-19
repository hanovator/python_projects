from django import forms
from django.contrib.auth.models import User


# 회원가입 폼 모델클래스
class UserForm(forms.ModelForm):
    class Meta:  # 폼 클래스를 생성하기 위한 정보를 제공하는 내부클래스
        model = User  # django에 내장된 User 클래스의 인스턴스 생성
        # 회원가입 폼에 사용할 필드정의
        fields = ["username", "email", "password"]


# 로그인폼 모델클래스
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
