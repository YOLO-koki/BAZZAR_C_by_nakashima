# from django.contrib.auth import get_user_model

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class CustomUserCreationForm(UserCreationForm):

#   def __init__(self, *args, **kwargs): # emailの登録を必須に変更
#       super().__init__(*args, **kwargs)
#       self.fields["email"].required = True

#   class Meta:
#     model = get_user_model()
#     fields = ["userid","username","password", "email", "phone"] 
#     labels = {
#       "userid": "ユーザーID",
#       "username": "ユーザー名",
#       "password": "パスワード",
#       "email": "メールアドレス",
#       "phone": "電話番号",
#     }
#     help_texts = {
#        "username": "",
#       "userid": "",
#       "password": "",
#       "email": "",
#       "phone": "",
#     }

# class CustomUserChangeForm(UserChangeForm):
#   def __init__(self, *args, **kwargs): # emailの登録を必須に変更
#       super().__init__(*args, **kwargs)
#       self.fields["email"].required = True

#   class Meta:
#     model = get_user_model()
#     fields = ["userid","username","password", "email", "phone"]
#     labels = {
#       "userid": "ユーザーID",
#       "username": "ユーザー名",
#       "password": "パスワード",
#       "email": "メールアドレス",
#       "phone": "電話番号",
#     }
#     help_texts = {
#        "username": "",
#       "userid": "",
#       "password": "",
#       "email": "",
#       "phone": "",
#     }