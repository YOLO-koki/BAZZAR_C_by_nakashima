from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.urls import reverse_lazy
 
class UserReviewPerfectView(TemplateView):
    template_name = "user/user_review_perfect.html"
    