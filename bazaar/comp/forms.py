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
