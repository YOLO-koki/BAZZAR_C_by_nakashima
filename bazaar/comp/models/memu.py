from django.db import models
#from .business_person import Business_person

from accounts.models import CustomUser
from .store import Store

#メニューのModel
class Menu(models.Model):
   #store_id,menu_name,sizeの合同主キー
   store_id=models.ForeignKey(Store,to_field='store_id',verbose_name='店舗ID',on_delete=models.PROTECT)
   menu_name=models.CharField(verbose_name='メニュー名',max_length=50)
   size=models.CharField(verbose_name='サイズ',max_length=3) 
   price=models.IntegerField(verbose_name='値段')
   photo1=models.ImageField(verbose_name='写真1',blank=True,null=True)
   photo2=models.ImageField(verbose_name='写真2',blank=True,null=True)
   photo3=models.ImageField(verbose_name='写真3',blank=True,null=True)
   photo4=models.ImageField(verbose_name='写真4',blank=True,null=True)
   photo5=models.ImageField(verbose_name='写真5',blank=True,null=True)