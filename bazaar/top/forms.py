from django import forms

def clean_Inquiry_email(value):
    if '@' not in value:
        raise forms.ValidationError('@を含んだメールアドレスにしてください')
    return value

class InquiryForm(forms.Form):
    Inquiry = forms.CharField(label = "お問い合わせ内容" , required = True ,widget = forms.Textarea)
    Inquiry_name = forms.CharField(label = "お名前" , required = True , max_length = 20, widget = forms.TextInput)
    Inquiry_email = forms.EmailField(label = "メールアドレス" ,validators=[clean_Inquiry_email], required = True , max_length = 50, widget = forms.TextInput,)
