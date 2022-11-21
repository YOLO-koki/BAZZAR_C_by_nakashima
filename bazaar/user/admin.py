from django.contrib import admin
from .models.users import User

# Register your models here.

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    model = User