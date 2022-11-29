from django.views.generic import FormView
from django.shortcuts import render
from ..forms import KutikomiForm

class UserKutikomiView(FormView):
    template_name = "user/user_make_review.html"
    form_class = KutikomiForm