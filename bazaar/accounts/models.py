from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,AbstractUser
"""
class UserType(models.Model):
    
    typename = models.CharField(verbose_name='ユーザ種別',
                                max_length=150)

    def __str__(self):
        return f'{self.id} - {self.typename}'

USERTYPE_COMP = 100
USERTYPE_USER = 200
USERTYPE_DEFAULT = USERTYPE_USER
"""


class CustomUser(AbstractUser,PermissionsMixin):
    #ユーザーと事業者共通で必要
    userid = models.AutoField(verbose_name='userid',primary_key=True)
    username = models.CharField(verbose_name='name', max_length=20,unique=True)
    #Trueが一般ユーザー,Falseが事業者
    usertype = models.BooleanField(verbose_name='usertype',blank=True, null=True,default=True)
    password = models.CharField(verbose_name='password', max_length=128)
    mail=models.EmailField(verbose_name='メールアドレス',max_length=40)
    phone=models.CharField(verbose_name='電話番号',max_length=11,blank=True, null=True)
    #事業者のみで必要
    age=models.IntegerField(verbose_name='年齢',blank=True, null=True)
    adress=models.CharField(verbose_name='住所',max_length=80,blank=True, null=True)
    last_login = models.DateTimeField(verbose_name='lastlogin', blank=True, null=True)

    class Meta():
        verbose_name_plural = 'CustomUser'


