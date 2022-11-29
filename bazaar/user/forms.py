from django import forms
import sys
import pathlib
currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir)+"..comp/")
# from comp.models.business_person import Business_person
from.models.users import User 
from accounts.models import CustomUser
import re
from django.core.exceptions import ValidationError
from django.shortcuts import render


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



# class RegisterForm(forms.Form):
#     userId=forms.CharField(label='ユーザーID',min_length=8,max_length=16)
#     password=forms.CharField(label='パスワード',min_length=8,max_length=16,widget=forms.PasswordInput,)
#     rePassword=forms.CharField(label='パスワード(再入力)',min_length=8,max_length=16,widget=forms.PasswordInput)
#     name=forms.CharField(label='名前',max_length=20)
#     mail=forms.EmailField(label='メールアドレス',max_length=40)
#     phone = forms.CharField(label='電話番号' ,max_length = 16)


#     def clean(self):
#          password = self.cleaned_data.get('password')
#          rePassword=self.cleaned_data.get('rePassword')

#          if password!=rePassword:
#              raise ValidationError("パスワードが一致しません。")
    
#     def send(inf):
#       return render(request="post",template_name="user/user_check_registed_info.html",context=inf)
class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(RegisterForm, self).__init__(*args, **kwd)
    class Meta:
        model=User
        fields=('userId','password','rePassword','name','mail','phone')
        labels = {
            'userId': 'ユーザーID',
            'password': 'パスワード',
            'rePassword':'パスワード(再入力)',
            'name':'名前',
            'mail':'メールアドレス',
            'phone':'電話番号',
        }
        widgets = {
            'userId': forms.TextInput,
            'password': forms.PasswordInput,
            'rePassword': forms.PasswordInput,
            'name':forms.TextInput,
            'mail': forms.EmailInput,
            'phone':forms.TextInput,
        }

    def clean(self):
        password = self.cleaned_data.get('password')
        rePassword=self.cleaned_data.get('rePassword')

        if password!=rePassword:
            raise ValidationError("パスワードが一致しません。")
        
    
    
      

        