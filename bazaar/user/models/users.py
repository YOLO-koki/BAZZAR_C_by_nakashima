from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError


class User(models.Model):
    userId=models.CharField(verbose_name='ユーザーID',max_length=16,primary_key=True, validators=[MinLengthValidator(8, '8文字以上です'),RegexValidator(r'^[a-zA-Z0-9]*$', '英数字のみです！')])
    password=models.CharField(verbose_name='パスワード',max_length=20,validators=[MinLengthValidator(8, '8文字以上です'),RegexValidator(r'^[a-zA-Z0-9]*$', '英数字のみです！'),])
    rePassword=models.CharField(verbose_name='パスワード',max_length=20,validators=[MinLengthValidator(8, '8文字以上です'),RegexValidator(r'^[a-zA-Z0-9]*$', '英数字のみです！')])
    name=models.CharField(verbose_name='名前',max_length=20)
    mail=models.CharField(verbose_name='メールアドレス',max_length=40)
    phone = models.CharField( max_length = 16, verbose_name='電話番号')