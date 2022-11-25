from django.db import models 
from .business_person import Business_person
from user.models.users import User

class Kuchikomi(models.Model):
   bp_id=models.ForeignKey(Business_person,to_field='bp_id',verbose_name='事業者ID',on_delete=models.PROTECT) 
   user_id=models.ForeignKey(User,to_field='userId',verbose_name='ユーザーID',on_delete=models.PROTECT)
   score=models.IntegerField(verbose_name='評価点数')
   impression=models.TextField(verbose_name='評価内容',max_length=2000)