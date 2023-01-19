from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from django .shortcuts import redirect
from comp.models import Store

 
class UserReviewPerfectView(TemplateView):
    template_name = "user/user_review_perfect.html"