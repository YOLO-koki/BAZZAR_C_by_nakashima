from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from ..forms import send_email
 
class CoInquiryPerfectView(TemplateView):
    template_name = "top/co_inquiry_perfect.html"


    def __init__(self): #hiddenから受け取り
        self.params = {
        'inquiry':'',
        'Inquiry_name':'',
        'Inquiry_email':'',
        }

    def post(self,request):
        inquiry = request.POST['inquiry']
        inquiry_name = request.POST['inquiry_name']
        inquiry_email = request.POST['inquiry_email']
        self.params["inquiry"] = inquiry
        self.params["inquiry_name"] = inquiry_name
        self.params["inquiry_email"] = inquiry_email
        abc = self.params

        sent_email(abc) #メール送信

        return render(request,'top/co_inquiry_perfect.html',abc)
    
def sent_email(abc):#メール送信
    send_email(abc)
