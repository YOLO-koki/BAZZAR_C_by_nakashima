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
#from django.contrib.auth.forms.UserCreationForm import clean_password2


# class LoginBusiness_personForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('userid', 'password')
#         labels = {
#             'userid': 'ユーザーID',
#             'password': 'パスワード',
#         }
#         widgets = {
#             'userid': forms.TextInput,
#             'password': forms.TextInput,
#         }



class RegisterForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['usertype'].widget.initial = False

    userid=forms.CharField(label='ユーザーID',min_length=8,max_length=16)
    usertype=forms.BooleanField(initial=False)
    #password1=forms.CharField(label='パスワード',min_length=8,max_length=16,widget=forms.PasswordInput)
    #password2=forms.CharField(label='パスワード(再入力)',min_length=8,max_length=16,widget=forms.PasswordInput)
    username=forms.CharField(label='名前',max_length=20)
    mail=forms.EmailField(label='メールアドレス',max_length=40)
    phone = forms.CharField(label='電話番号' ,max_length = 16)


    class Meta:
        model=CustomUser
        
        fields =(CustomUser.USERNAME_FIELD,'username','age','mail','phone','adress', 'usertype','age')
        labels= {
            'userid':'ユーザーID',
            'username':'名前',
            'age':'年齢',
            'mail':'メールアドレス',
            'phone':'電話番号',
            'adress':'住所',
        }

class SaveForm(forms.Form):
    userid=forms.CharField(label='ユーザーID',min_length=8,max_length=16)
    password=forms.CharField(label='パスワード',min_length=8,max_length=16,widget=forms.PasswordInput)
    confirm_password=forms.CharField(label='パスワード(再入力)',min_length=8,max_length=16,widget=forms.PasswordInput)
    username=forms.CharField(label='名前',max_length=20)
    mail=forms.EmailField(label='メールアドレス',max_length=40)
    phone = forms.CharField(label='電話番号' ,max_length = 16)    
    



       
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class LoginCustomUserForm(AuthenticationForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['userid'].widget = forms.TextInput(attrs={'required': 'true', 'placeholder': 'ユーザーID'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'required': 'true', 'placeholder': 'パスワード'})
        self.fields['userid'].widget.attrs['name'] = 'userid'
        self.fields['password'].widget.attrs['name'] = 'password'

        # username = self.fields['userid']
        # password = self.fields['password']

        # username.widget = forms.TextInput(attrs={'required': 'true', 'placeholder': 'ユーザーID'})
        # password.widget = forms.PasswordInput(attrs={'required': 'true', 'placeholder': 'パスワード'})
        

    class Meta:
        model = CustomUser
        fields = ('userid', 'password')
        labels = {
            'userid': '事業者ID',
            'password': 'パスワード',
        }
