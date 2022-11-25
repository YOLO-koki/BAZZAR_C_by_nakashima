# from django.db import models
# from accounts.models import CustomUser

# class User(models.Model):
#     user_id=models.ForeignKey(CustomUser,to_field='userid',verbose_name='会員ID',on_delete=models.PROTECT) 
#     password=models.ForeignKey(CustomUser,to_field='password',verbose_name='パスワード',max_length=20,on_delete=models.PROTECT)
#     name=models.ForeignKey(CustomUser,to_field='username',verbose_name='名前',max_length=20,on_delete=models.PROTECT)
#     mail=models.ForeignKey(CustomUser,to_field='mail',verbose_name='メールアドレス',max_length=40,on_delete=models.PROTECT)
#     phone=models.ForeignKey(CustomUser,to_field='phone',verbose_name='電話番号',max_length=11,on_delete=models.PROTECT)