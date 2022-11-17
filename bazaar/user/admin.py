from django.contrib import admin
from .models.user import User

# Register your models here.

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    model = User