from django import forms
import sys
import pathlib
currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir)+"..comp/")
# from comp.models.business_person import Business_person
# from.models.users import User
from accounts.models import CustomUser
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from comp.models import Kuchikomi
from comp.models import Reservation
#from django.contrib.auth.forms.UserCreationForm import clean_password2


class LoginBusiness_personForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('userid', 'password')
        labels = {
            'userid': 'ユーザーID',
            'password': 'パスワード',
        }
        widgets = {
            'userid': forms.TextInput,
            'password': forms.TextInput,
        }



class RegisterForm(UserCreationForm):
    userid=forms.CharField(label='ユーザーID',min_length=8,max_length=16)
    password1=forms.CharField(label='パスワード',min_length=8,max_length=16,widget=forms.PasswordInput)
    password2=forms.CharField(label='パスワード(再入力)',min_length=8,max_length=16,widget=forms.PasswordInput)
    username=forms.CharField(label='名前',max_length=20)
    mail=forms.EmailField(label='メールアドレス',max_length=40)
    phone = forms.CharField(label='電話番号' ,max_length = 16)

    class Meta:
        model=CustomUser
        fields =(CustomUser.USERNAME_FIELD,'username','mail','phone')
        labels= {
            'userid':'ユーザーID',
            'username':'名前',
            'mail':'メールアドレス',
            'phone':'電話番号',
        }

        
        

class SaveForm(forms.Form):
    
    userid=forms.CharField(label='ユーザーID',min_length=8,max_length=16)
    password=forms.CharField(label='パスワード',min_length=8,max_length=16,widget=forms.PasswordInput)
    confirm_password=forms.CharField(label='パスワード(再入力)',min_length=8,max_length=16,widget=forms.PasswordInput)

    # username=forms.CharField(label='名前',max_length=20)
    # mail=forms.EmailField(label='メールアドレス',max_length=40)
    # phone = forms.CharField(label='電話番号' ,max_length = 16)  

    
class KutikomiForm(forms.ModelForm):
    class Meta:
        model = Kuchikomi
        fields = ('store_id','user_id','score','impression',)
        exclude = ["store_id"]

class ReservationForm(forms.ModelForm):
    class Meta:
        model= Reservation
        exclude = ["store_id","user_id","menu1","menu2","menu3","menu4","menu5"]
