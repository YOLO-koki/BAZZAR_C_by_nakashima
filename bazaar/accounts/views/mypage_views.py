from django.views.generic import TemplateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from comp.models import Store,Menu


#ログインしていることが条件
class MypageView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/mypage.html"

    def get(self, request, **kwargs):
        ctx = {
            'usertype': self.request.user.usertype
        }
        return self.render_to_response(ctx)

    def get_object(self):
        id=Store.objects.get(bp_id_id=self.request.user)
        store = Store.objects.filter(store_id=id).exists

        # menu_id = Store.objects.get(bp_id_id=self.request.user)
        # menu = Menu.objects.filter(store_id_id = menu_id).exists
        return store