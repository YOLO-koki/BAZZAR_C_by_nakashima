from django.views.generic import FormView
from django.shortcuts import render
from ..forms import KutikomiForm
from django.urls import reverse_lazy
from comp.models import Store,Kuchikomi
from django .shortcuts import redirect

class UserKutikomiView(FormView):
    model = Kuchikomi
    template_name = "user/user_make_review.html"
    form_class = KutikomiForm
    success_url = reverse_lazy('user:userReviewPerfect')
    context_object_name = 'stores'

    def form_valid(self, form):
        kuchikomi_content=form.save(commit=False)
        store_id = Store.objects.get(store_id=self.kwargs['pk'])
        kuchikomi_content.store_id=store_id
        kuchikomi_content.user_id=self.request.user
        kuchikomi_content.save()
        return redirect('user:userReviewPerfect')

    def get_context_data(self, **kwargs):
        context = super(UserKutikomiView,self).get_context_data(**kwargs)
        context.update({
            'kuchikomi_list':Kuchikomi.objects.all()
        })
        return context

    def get_queryset(self):
        return Store.objects.all()

      #ユーザID用

    # def form_valid(self, form):
    #     user_id=form.save(commit=False)  # 保存処理など
    #     user_id.user_id=self.request.user
    #     user_id.save()
    #     return redirect('top:detail')