from django.views.generic import FormView
from ..forms import ReservationLoginForm
from django.shortcuts import render
from comp.models import Store
from accounts.models import CustomUser
class UserMakeReservationLoginView(FormView):
    template_name: str = "user/user_make_reservation.html"
    form_class=ReservationLoginForm
    success_url = 'top:toppage'
    def form_valid(self,form):
        hoge=form.save(commit=False)
        hoge.store_id=Store.objects.get(store_id=self.kwargs['pk'])
        fuga=CustomUser.objects.get(userid=self.request.user)
        hoge.reservation_name=fuga.username
        hoge.reservation_phone=fuga.phone
        hoge.reservation_mail=fuga.mail
        hoge.save()
        return render(request=self.request,template_name="top/co_toppage.html",context={'store':hoge})