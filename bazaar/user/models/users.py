from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    user_id=models.CharField(verbose_name='ユーザーID',max_length=16,primary_key=True)
    password=models.CharField(verbose_name='パスワード',max_length=20)
    name=models.CharField(verbose_name='名前',max_length=20)
    mail=models.CharField(verbose_name='メールアドレス',max_length=40)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True,verbose_name='電話番号')