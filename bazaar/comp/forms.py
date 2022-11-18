from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models.business_person import Business_person


class LoginBusiness_personForm(forms.ModelForm):
    class Meta:
        model = Business_person
        fields = ('bp_id', 'password')
        labels = {
            'bp_id': '事業者ID',
            'password': 'パスワード',
        }
        widgets = {
            'bp_id': forms.TextInput,
            'password': forms.TextInput,
        }
