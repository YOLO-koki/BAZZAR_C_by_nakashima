from django.db import models
# from .business_person import Business_person
from accounts.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator

#店舗のModel

class Store(models.Model):
    
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
    #store_idが主キー
    store_id = models.AutoField(verbose_name='storeid',primary_key=True)
    bp_id=models.ForeignKey(CustomUser,to_field='userid',verbose_name='事業者ID',max_length=16,on_delete=models.PROTECT)
    store_name=models.CharField(verbose_name='店舗名',max_length=30)
    #CustomUserのほうが事業者の住所,Storeのほうが店舗の住所.
    postal_code=models.CharField(verbose_name='郵便番号',max_length=8)
    adress1=models.CharField(verbose_name='住所(xx県xx市)',max_length=20)
    adress2=models.CharField(verbose_name='住所(xx丁目xx番地)',max_length=20)
    adress3=models.CharField(verbose_name='住所(ビル名など)',max_length=20)
    phone_number=models.CharField(verbose_name='電話番号',max_length=13)
    #seatが店全体の席数。seat_reservationableが時間ごとに予約可能な席数
    seat=models.IntegerField(verbose_name='席数',validators=[MinValueValidator(0)])
    seat_reservationable=models.IntegerField(verbose_name='予約可能な席数',validators=[MinValueValidator(0)])
    bussiness_hours_start=models.CharField(verbose_name='営業開始',max_length=3,choices=hour,default="選択してください")
    start_minute=models.CharField(verbose_name="",max_length=3,choices=minute,default="選択してください")
    bussiness_hours_end=models.CharField(verbose_name='営業終了',max_length=3,choices=hour,default=df)
    end_minute=models.CharField(verbose_name="", max_length=3,choices=minute ,default="選択してください")
    holiday1=models.CharField(verbose_name="定休日1" ,max_length=4,choices=date,default=cel)
    holiday2=models.CharField(verbose_name="定休日2" ,max_length=4,choices=date,default=none)
    holiday3=models.CharField(verbose_name="定休日3" ,max_length=4,choices=date,default=none)
    photo1=models.ImageField(verbose_name='写真1',blank=True,null=True)
    photo2=models.ImageField(verbose_name='写真2',blank=True,null=True)
    photo3=models.ImageField(verbose_name='写真3',blank=True,null=True)
    photo4=models.ImageField(verbose_name='写真4',blank=True,null=True)
    photo5=models.ImageField(verbose_name='写真5',blank=True,null=True)
    photo6=models.ImageField(verbose_name='写真6',blank=True,null=True)
    photo7=models.ImageField(verbose_name='写真7',blank=True,null=True)
    photo8=models.ImageField(verbose_name='写真8',blank=True,null=True)
    photo9=models.ImageField(verbose_name='写真9',blank=True,null=True)
    photo10=models.ImageField(verbose_name='写真10',blank=True,null=True)
    about=models.TextField(verbose_name='紹介文',max_length=300)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['bp_id'], name='unique_bo')
        ]
