from django.views.generic import FormView
from django.shortcuts import render
from ..forms import KutikomiForm
from django.urls import reverse_lazy
from comp.models import Store,Kuchikomi

class UserKutikomiView(FormView):
    model = Store
    template_name = "user/user_make_review.html"
    form_class = KutikomiForm
    success_url = reverse_lazy('user:userCheckKutikomi')
    context_object_name = 'stores'


    def form_valid(self,form):
        return render(request=self.request, template_name = "user/user_review_check.html" ,context = {'form':form})

    def get_context_data(self, **kwargs):
        context = super(UserKutikomiView,self).get_context_data(**kwargs)
        context.update({
            'kuchikomi_list':Kuchikomi.objects.all()
        })
        return context

    def get_queryset(self):
        return Store.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # store_id_data = 
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     data_list = Store.objects.filter(store_id = self.kwargs['pk'])

    #     context['store_data_list'] = data_list
    #     return context


    # def post(self, **kwargs):
    #         kwargs['store_id']

      #ユーザID用

    # def form_valid(self, form):
    #     user_id=form.save(commit=False)  # 保存処理など
    #     user_id.user_id=self.request.user
    #     user_id.save()
    #     return redirect('top:detail')