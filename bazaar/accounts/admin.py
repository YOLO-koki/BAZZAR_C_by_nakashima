from django.contrib import admin

from .models import CustomUser

admin.site.register(CustomUser)

# @admin.register()
# class CustomUser(admin.ModelAdmin):
#     model:CustomUser
