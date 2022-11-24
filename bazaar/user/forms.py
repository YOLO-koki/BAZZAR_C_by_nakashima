from django import forms
from django.contrib.auth.forms import AuthenticationForm
import sys
import pathlib
currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir)+"..comp/")
from comp.models.business_person import Business_person
from.models.users import User 
import re

class LoginBusiness_personForm(forms.ModelForm):
    class Meta:
        model = Business_person
        fields = ('bp_id', 'password')
        labels = {
            'bp_id': 'ユーザーID',
            'password': 'パスワード',
        }
        widgets = {
            'bp_id': forms.TextInput,
            'password': forms.TextInput,
        }



class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields= ('user_id', 'password','name','mail','phone')
        labels={
            'user_id':'ユーザーID(8~16文字)',
            'password':'パスワード(8~16文字)',
            'name':'名前',
            'mail':'メールアドレス',
            'phone':'電話番号',
        }
        widgets={
            'user_id':forms.TextInput,
            'password':forms.TextInput,
            'name':forms.TextInput,
            'mail':forms.EmailInput,
            'phone':forms.TextInput,
        }
        def clean_regi_email(self):
           regi_email = self.cleaned_data['mail']
           if '@' not in regi_email:
              raise forms.ValidationError('@を含んだメールアドレスにしてください')
           return regi_email
        
        def clean_tel(self):
           phone_num = self.cleaned_data['phone']
           if not re.match(r'^\d{2,4}-\d{2,4}-\d{4}$', phone_num):
                raise forms.ValidationError(u'正しい電話番号を入力して下さい(ハイフン不要)')
           return phone_num