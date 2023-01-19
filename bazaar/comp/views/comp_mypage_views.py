from django.shortcuts import render
from ..models import Store
from django.views.generic import TemplateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

#ログインしていることが条件
class CompMypageView(LoginRequiredMixin, TemplateView):
    template_name = "comp/bo_mypage.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     hoge=Store.objects.filter(bp_id=self.request.user)

    # #get処理
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

    # #post処理
    # def post(self, request, *args, **kwargs):
    #     self.kwargs["message"] = "Post処理"
    #     return render(request, self.template_name, context=self.kwargs)