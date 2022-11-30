from django.db import models
# from user.models.users import User
# from .business_person import Business_person
from .memu import Menu
from accounts.models import CustomUser
from .store import Store

#予約のModel
class Reservation(models.Model):
   #store_id,user_id,timeの合同主キー
   store_id=models.ForeignKey(Store,to_field='store_id',verbose_name='店舗ID',on_delete=models.PROTECT) 
   user_id=models.ForeignKey(CustomUser,to_field='userid',verbose_name='ユーザーID',max_length=16,on_delete=models.PROTECT,null=True,blank=True)
   menu1=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー1',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_1')
   menu2=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー2',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_2')
   menu3=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー3',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_3')
   menu4=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー4',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_4')
   menu5=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー5',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_5')
   time=models.TimeField(verbose_name='予約日時')
   nop=models.IntegerField(verbose_name='予約人数')
   reservation_name=models.CharField(verbose_name='予約者名',max_length=20,null=True,blank=True)
   reservation_mail=models.CharField(verbose_name='予約者メールアドレス',max_length=40,null=True,blank=True)
   reservation_phone=models.CharField(verbose_name='予約者電話番号',max_length=11,null=True,blank=True)