from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class CoInquiryView(TemplateView):
    template_name = "top/co_inquiry.html"