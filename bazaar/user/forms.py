from django import forms
import sys
import pathlib
currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir)+"..comp/")
# from comp.models.business_person import Business_person
# from.models.users import User
from comp.models.kuchikomi import Kuchikomi
from accounts.models import CustomUser
import re
from django.core.exceptions import ValidationError


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



class RegisterForm(forms.Form):
    userId=forms.CharField(label='ユーザーID',min_length=8,max_length=16)
    password=forms.CharField(label='パスワード',min_length=8,max_length=16,widget=forms.PasswordInput)
    rePassword=forms.CharField(label='パスワード(再入力)',min_length=8,max_length=16,widget=forms.PasswordInput)
    name=forms.CharField(label='名前',max_length=20)
    mail=forms.EmailField(label='メールアドレス',max_length=40)
    phone = forms.CharField(label='電話番号' ,max_length = 16)


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('rePassword')
        if password != confirm_password:
            self.add_error(
               field='rePassword',
               error=ValidationError('パスワードが一致しません'))
        return cleaned_data

       
class KutikomiForm(forms.ModelForm):
    class Meta:
        model = Kuchikomi
        fields = ('store_id','user_id','score','impression',)


