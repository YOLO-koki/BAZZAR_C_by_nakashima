from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from comp.models.kuchikomi import Kuchikomi
from accounts.models import CustomUser
from comp.models.store import Store
from ..forms import KutikomiForm
# from ..forms import RegisterForm

# from django.core.exceptions import ValidationError

class UserCheckKutikomiView(CreateView):
    template_name = "user/user_review_check.html"
    model = Kuchikomi,CustomUser,Store
    form_class = KutikomiForm
    success_url = reverse_lazy('user:userReviewPerfect')