from django.db import models 
# from .business_person import Business_person
# import sys
import pathlib
currentdir = pathlib.Path(__file__).resolve().parent
#sys.path.append(str(currentdir)+"..user/")
#from user.models.users import User

from accounts.models import CustomUser
from .store import Store

class Kuchikomi(models.Model):
   store_id=models.ForeignKey(Store,to_field='store_id',verbose_name='店舗ID',on_delete=models.PROTECT) 
   user_id=models.ForeignKey(CustomUser,to_field='userid',verbose_name='ユーザーID',max_length=16,on_delete=models.PROTECT)
   score=models.IntegerField(verbose_name='評価点数')
   impression=models.TextField(verbose_name='評価内容',max_length=2000)