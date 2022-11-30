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

class KutikomiForm(forms.ModelForm):
    class Meta:
        model = 
        fields = ('')

       

        
# stars_list = [('1','星１'),('2','星２'),('3','星３'),('4','星４'),('5','星５')]

# class KutikomiForm(forms.Form):
#     stars = forms.CharField(label="評価",required=True,widget=forms.RadioSelect)
#     impressions = forms.CharField(label="感想",required=True)