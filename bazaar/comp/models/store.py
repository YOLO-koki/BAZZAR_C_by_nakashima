from django.db import models
# from .business_person import Business_person
from accounts.models import CustomUser

class Store(models.Model):
    store_id = models.AutoField(verbose_name='storeid',primary_key=True)
    bp_id=models.ForeignKey(CustomUser,to_field='userid',verbose_name='事業者ID',on_delete=models.PROTECT)
    store_name=models.CharField(verbose_name='店舗名',max_length=30)
    adress=models.CharField(verbose_name='住所',max_length=80)
    seat=models.IntegerField(verbose_name='席数')
    seat_reservationable=models.ImageField(verbose_name='予約可能な席数')
    bussiness_hours=models.TimeField(verbose_name='営業時間')
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