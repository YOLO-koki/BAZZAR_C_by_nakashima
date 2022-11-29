from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class LoginCustomUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['userid'].widget = forms.TextInput(attrs={'required': 'true'})
        self.fields['password'].widget = forms.TextInput(attrs={'required': 'true'})

    class Meta:
        model = CustomUser
        fields = ('userid', 'password',)
        labels = {
            'userid': '事業者ID',
            'password': 'パスワード',
        }
