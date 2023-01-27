from django.db import models
# from user.models.users import User
# from .business_person import Business_person
from .memu import Menu
from accounts.models import CustomUser
from .store import Store
from django.utils import timezone
from bootstrap_datepicker_plus.widgets import DatePickerInput
#予約のModel

class Reservation(models.Model):
   #store_id,user_id,timeの合同主キー
   mon="mon"
   tue="tue"
   wed="wed"
   thr="thr"
   fri="fri"
   sat="sat"
   sun="sun"
   cel="祝日"
   none="なし"
   date=[
      ('月曜日','月曜日'),
      ('火曜日','火曜日'),
      ('水曜日','水曜日'),
      ('木曜日','木曜日'),
      ('金曜日','金曜日'),
      ('土曜日','土曜日'),
      ('日曜日','日曜日'),
      ('祝日','祝日'),
      ('なし','なし')
    ]
   df="選択してください"
   hour=[
      ("１時","１時"),
      ("2時","2時"),
      ("3時","3時"),
      ("4時","4時"),
      ("5時","5時"),
      ("6時","6時"),
      ("7時","7時"),
      ("8時","8時"),
      ("9時","9時"),
      ("10時","10時"),
      ("11時","11時"),
      ("12時","12時"),
      ("13時","13時"),
      ("14時","14時"),
      ("15時","15時"),
      ("16時","16時"),
      ("17時","17時"),
      ("18時","18時"),
      ("19時","19時"),
      ("20時","20時"),
      ("21時","21時"),
      ("22時","22時"),
      ("23時","23時"),
      ("24時","24時"),
    ]
   minute=[
      ("00分","00分"),
      ("15分","15分"),
      ("30分","30分"),
      ("45分","45分"),
    ]
   store_id=models.ForeignKey(Store,to_field='store_id',verbose_name='店舗ID',on_delete=models.PROTECT) 
   user_id=models.ForeignKey(CustomUser,to_field='userid',verbose_name='ユーザーID',max_length=16,on_delete=models.PROTECT,null=True,blank=True)
   menu1=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー1',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_1')
   menu2=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー2',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_2')
   menu3=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー3',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_3')
   menu4=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー4',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_4')
   menu5=models.ForeignKey(Menu,to_field='id',verbose_name='メニュー5',on_delete=models.PROTECT,blank=True,null=True,related_name='menu_5')
   reservation_name=models.CharField(verbose_name='予約者名',max_length=20,null=True,blank=True)
   reservation_mail=models.CharField(verbose_name='予約者メールアドレス',max_length=40,null=True,blank=True)
   reservation_day=models.DateField(verbose_name='予約希望日',default=timezone.now)
   reservation_phone=models.CharField(verbose_name='予約者電話番号',max_length=11,null=True,blank=True)
   reservation_hour=models.CharField(verbose_name='予約希望時間',max_length=3,choices=hour,default="選択してください")
   reservation_minute=models.CharField(verbose_name="", max_length=3,choices=minute ,default="選択してください")
   nop=models.IntegerField(verbose_name='予約人数')
   
