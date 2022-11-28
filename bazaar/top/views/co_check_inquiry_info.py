from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from django.urls import reverse_lazy

class CoCheckInquiryInfoView(FormView):
    template_name = "top/co_check_inquiry_info.html"

    def __init__(self):#formの値の受け取り
        self.params = {
        'inquiry':'',
        'Inquiry_name':'',
        'Inquiry_email':'',
        }
    
    def post(self, request):
        inquiry = request.POST["inquiry"]
        inquiry_name = request.POST["inquiry_name"]
        inquiry_email = request.POST["inquiry_email"]
        self.params["inquiry"] = inquiry
        self.params["inquiry_name"] = inquiry_name
        self.params["inquiry_email"] = inquiry_email
        df = self.params

        return render(request, 'top/co_check_inquiry_info.html', df)