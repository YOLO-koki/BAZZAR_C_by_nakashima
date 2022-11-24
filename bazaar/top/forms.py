from django import forms
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.contrib import messages
from django.utils.datastructures import MultiValueDict
from django.core.mail import EmailMultiAlternatives

class InquiryForm(forms.Form):
    inquiry = forms.CharField(label = "お問い合わせ内容" , required = True ,widget = forms.Textarea)
    inquiry_name = forms.CharField(label = "お名前" , required = True , max_length = 20, widget = forms.TextInput)
    inquiry_email = forms.EmailField(label = "メールアドレス" , required = True , max_length = 50, widget = forms.TextInput)

    def clean_Inquiry_email(self):
        inquiry_email = self.cleaned_data['Inquiry_email']
        if '@' not in inquiry_email:
            raise forms.ValidationError('@を含んだメールアドレスにしてください')
        return inquiry_email

# class CoCheckInquiryInfoForm(forms.Form):

#     def send_email(self):
#         inquiry = self.cleaned_data['inquiry']
#         inquiry_name = self.cleaned_data['inquiry_name']
#         inquiry_email = self.cleaned_data['inquiry_email']

#         subject = "お問い合わせ"
#         message = "お問い合わせ内容:{0}\nお名前:{1}\nメールアドレス:{2}".format(inquiry,inquiry_name,inquiry_email)
#         from_email = 'admin@example.com'
#         to_list = [
#             'test@example.com'
#         ]
#         cc_list = [
#             inquiry_email
#         ]

#         message = EmailMessage(subject = subject , body = message, from_email = from_email, to = to_list, cc = cc_list)
#         message.send()

def send_email():
	mail_title="email_title"
	text_content="hello"
	html_content="<p><strong>※このメールに返信はできません</strong></p>"

	msg=EmailMultiAlternatives(
        subject=mail_title,
        body=text_content,
        from_email="admin_email",
        to=["admin_email"],
        reply_to=[]
	)
	msg.attach_alternative(html_content,"top/co_check_inquiry_info.html")
	msg.send()