from django.db import models

class User(models.Model):
    userId=models.CharField(verbose_name='ユーザーID',max_length=16,primary_key=True)
    password=models.CharField(verbose_name='パスワード',max_length=20)
    rePassword=models.CharField(verbose_name='パスワード',max_length=20)
    name=models.CharField(verbose_name='名前',max_length=20)
    mail=models.CharField(verbose_name='メールアドレス',max_length=40)
    phone = models.CharField( max_length = 16, verbose_name='電話番号')