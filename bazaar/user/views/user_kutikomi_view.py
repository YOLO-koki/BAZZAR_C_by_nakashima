from django.views.generic import FormView
from django.shortcuts import render
from ..forms import KutikomiForm
from django.urls import reverse_lazy

class UserKutikomiView(FormView):
    template_name = "user/user_make_review.html"
    form_class = KutikomiForm
    success_url = reverse_lazy('user:userCheckKutikomi')
    def form_valid(self,form):
        return render(request=self.request, template_name = "user/user_review_check.html" ,context = {'form':form})