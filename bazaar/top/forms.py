from django import forms

class InquiryForm(forms.Form):
    Inquiry = forms.CharField(label = "お問い合わせ内容" , required = True ,widget = forms.Textarea)
    Inquiry_name = forms.CharField(label = "お名前" , required = True , max_length = 20, widget = forms.TextInput)
    Inquiry_email = forms.EmailField(label = "メールアドレス" , required = True , max_length = 50, widget = forms.TextInput)

    def clean_Inquiry_email(self):
        Inquiry_email = self.cleaned_data['Inquiry_email']
        if '@' not in Inquiry_email:
            raise forms.ValidationError('@を含んだメールアドレスにしてください')
        return Inquiry_email


