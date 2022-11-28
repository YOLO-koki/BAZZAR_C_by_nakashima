from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator
from django.contrib.auth.models import BaseUserManager


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


alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, mail, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not mail:
            raise ValueError(('メールアドレスを入力してください'))
        mail = self.normalize_email(mail)
        user = self.model(mail=mail, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, mail, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(('Superuser must have is_superuser=True.'))

        def get_by_natural_key(self,email, password):
            return self.get(email = email, password=password)
        
        return self.create_user(mail,password)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    #ユーザーと事業者共通で必要
    #userid 主キー　１６桁
    userid = models.CharField(verbose_name='userid',
                          validators=[alphanumeric],primary_key=True,max_length=16,unique=True)
    username = models.CharField(verbose_name='name',max_length=20)
    #Trueが一般ユーザー,Falseが事業者
    usertype = models.BooleanField(verbose_name='usertype',default=True)
    password = models.CharField(verbose_name='password', max_length=128)
    mail=models.EmailField(verbose_name='mail',max_length=40)
    phone=models.CharField(verbose_name='tel',max_length=11,blank=True, null=True)
    #事業者のみで必要
    age=models.IntegerField(verbose_name='age',blank=True, null=True,validators=[MaxValueValidator(150),MinValueValidator(0)])
    adress=models.CharField(verbose_name='adress',max_length=80,blank=True, null=True)
    last_login = models.DateTimeField(verbose_name='lastlogin', blank=True, null=True)

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = [
       'mail'
    ]

    objects = CustomUserManager()

    class Meta():
        verbose_name_plural = 'CustomUser'

