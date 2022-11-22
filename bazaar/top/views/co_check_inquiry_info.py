from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from ..forms import InquiryForm

class CoCheckInquiryInfoView(TemplateView):
    template_name = "top/co_check_inquiry_info.html"

    def __init__(self):
        self.params = {
        'inquiry':'',
        'Inquiry_name':'',
        'Inquiry_email':'',
        }
    
    def post(self, request):
        Inquiry = request.POST["Inquiry"]
        Inquiry_name = request.POST["Inquiry_name"]
        Inquiry_email = request.POST["Inquiry_email"]
        self.params["inquiry"] = Inquiry
        self.params["inquiry_name"] = Inquiry_name
        self.params["inquiry_email"] = Inquiry_email
        df = self.params

        return render(request, 'top/co_check_inquiry_info.html', df)