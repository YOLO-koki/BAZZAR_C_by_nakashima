from django.db import models
from django.conf import settings
# from .business_person import Business_person
from accounts.models import CustomUser


#店舗のModel

class Store(models.Model):
    #store_idが主キー
    store_id = models.AutoField(verbose_name='storeid',primary_key=True)
    bp_id=models.ForeignKey(CustomUser,to_field='userid',verbose_name='事業者ID',max_length=16,on_delete=models.PROTECT)
    store_name=models.CharField(verbose_name='店舗名',max_length=30)
    #CustomUserのほうが事業者の住所,Storeのほうが店舗の住所.
    adress=models.CharField(verbose_name='住所',max_length=80)
    #seatが店全体の席数。seat_reservationableが時間ごとに予約可能な席数
    seat=models.IntegerField(verbose_name='席数')
    seat_reservationable=models.ImageField(verbose_name='予約可能な席数')
    bussiness_hours=models.TimeField(verbose_name='営業時間')
    photo1=models.ImageField(verbose_name='写真1',blank=True,null=True, upload_to='media/')
    photo2=models.ImageField(verbose_name='写真2',blank=True,null=True, upload_to='media/')
    photo3=models.ImageField(verbose_name='写真3',blank=True,null=True, upload_to='media/')
    photo4=models.ImageField(verbose_name='写真4',blank=True,null=True, upload_to='media/')
    photo5=models.ImageField(verbose_name='写真5',blank=True,null=True, upload_to='media/')
    photo6=models.ImageField(verbose_name='写真6',blank=True,null=True, upload_to='media/')
    photo7=models.ImageField(verbose_name='写真7',blank=True,null=True, upload_to='media/')
    photo8=models.ImageField(verbose_name='写真8',blank=True,null=True, upload_to='media/')
    photo9=models.ImageField(verbose_name='写真9',blank=True,null=True, upload_to='media/')
    photo10=models.ImageField(verbose_name='写真10',blank=True,null=True, upload_to='media/')

# photo1_filepath = Store.filter(id=store_id).values()[0]["photo1"]


# image_url = f"{settings.MEDIA_URL}/{photo1_filepath}"
