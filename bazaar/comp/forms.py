from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import CustomUser


class LoginBusiness_personForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usertype'].initial = False

    class Meta:
        model = CustomUser
        fields = ('userid', 'password')
        labels = {
            'userid': '事業者ID',
            'password': 'パスワード',
        }
        widgets = {
            'userid': forms.TextInput,
            'password': forms.TextInput,
        }
