from django.views.generic import TemplateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

#ログインしていることが条件
class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/mypage.html"

    def get(self, request, **kwargs):
        ctx = {
            'usertype': self.request.user.usertype
        }
        return self.render_to_response(ctx)