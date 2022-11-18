from django import forms

class InquiryForm(forms.Form):
    Inquiry = forms.CharField(label = 'お問い合わせ内容', max_length = 300)
    Inquiry_name = forms.CharField(label = 'お名前', max_length = 20)
    Inquiry_email = forms.EmailField(label = 'メールアドレス', max_length = 50)