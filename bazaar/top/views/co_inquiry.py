from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from django.urls import reverse_lazy
from ..forms import InquiryForm

class CoInquiryView(FormView):
    template_name = "top/co_inquiry.html"
    form_class = InquiryForm