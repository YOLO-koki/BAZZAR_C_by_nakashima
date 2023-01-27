from django.contrib import admin

# Register your models here.
#from .models.business_person import Business_person
from .models.kuchikomi import Kuchikomi
from .models.memu import Menu
from .models.store import Store
from .models.reservation import Reservation


# @admin.register(Business_person)
# class userAdmin(admin.ModelAdmin):
#     model = Business_person

@admin.register(Kuchikomi)
class userAdmin(admin.ModelAdmin):
    model = Kuchikomi 

@admin.register(Menu)
class userAdmin(admin.ModelAdmin):
    model = Menu 

@admin.register(Store)
class userAdmin(admin.ModelAdmin):
    model = Store

@admin.register(Reservation)
class userAdmin(admin.ModelAdmin):
    model = Reservation