from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


"""試作品
class UserType(models.Model):
    
    typename = models.CharField(verbose_name='ユーザ種別',
                                max_length=150)

    def __str__(self):
        return f'{self.id} - {self.typename}'

USERTYPE_COMP = 100
USERTYPE_USER = 200
USERTYPE_DEFAULT = USERTYPE_USER
"""
'''
alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
'''

class CustomUserManager(BaseUserManager):
    """
    ユーザーを作るときにEmailは絶対に必要
    """
    def _create_user(self, userid, mail,password,  **extra_fields):
        if not mail:
            raise ValueError('Emailを入力して下さい')
        mail = self.normalize_email(mail)
        userid = self.model.normalize_username(userid)
        user = self.model(userid=userid, mail=mail, **extra_fields)
        user.password = make_password(password)
        
        user.save(using=self.db)
        return user
    

    """

    """
    def create_user(self,userid, mail, password, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(userid,mail, password, **extra_fields)

    def create_superuser(self,userid, mail, password, **extra_fields):
        """

        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))

        def get_by_natural_key(self,mail, password):
            return self.get(mail = mail, password=password)
        
        return self._create_user(userid,mail, password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    #ユーザーと事業者共通で必要
    #userid 主キー　１６桁
    userid = models.CharField(verbose_name='userid',primary_key=True,max_length=16,unique=True)

    username = models.CharField(verbose_name='name',max_length=20)

    #Trueが一般ユーザー,Falseが事業者
    usertype = models.BooleanField(verbose_name='usertype',default=True)
    #一般ユーザー、事業者、両方必要
    password = models.CharField(verbose_name='password', max_length=128)

    mail=models.EmailField(verbose_name='mail',max_length=40)

    phone=models.CharField(verbose_name='tel',max_length=11,blank=True, null=True)
    #事業者のみで必要
    age=models.IntegerField(verbose_name='age',blank=True, null=True,validators=[MaxValueValidator(150),MinValueValidator(0)])
    adress=models.CharField(verbose_name='adress',max_length=80,blank=True, null=True)
    last_login = models.DateTimeField(verbose_name='lastlogin', blank=True, null=True)
    #アカウントの権限
    is_superuser = models.BooleanField(("superuser status"),default=False,)
    is_staff = models.BooleanField(("staff status"),default=False,)
    is_active = models.BooleanField(("active status"),default=True,)
    


    USERNAME_FIELD = 'userid'
    EMAIL_FIELD = 'mail'
    REQUIRED_FIELDS = [
        'mail',
    ]

    objects = CustomUserManager()

    class Meta():
        verbose_name_plural = 'CustomUser'


