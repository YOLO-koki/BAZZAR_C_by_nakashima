from django.contrib import admin

from .models import CustomUser

#管理者サイトにCustomUserを表示させている
admin.site.register(CustomUser)

# @admin.register()
# class CustomUser(admin.ModelAdmin):
#     model:CustomUser
