from django.db import models

class Business_person(models.Model):
    bp_id=models.CharField(verbose_name='事業者ID',max_length=16,primary_key=True)
    password=models.CharField(verbose_name='パスワード',max_length=20)
    name=models.CharField(verbose_name='名前',max_length=20)
    age=models.IntegerField(verbose_name='年齢')
    mail=models.CharField(verbose_name='メールアドレス',max_length=40)
    phone=models.CharField(verbose_name='電話番号',max_length=11)
    adress=models.CharField(verbose_name='住所',max_length=80)