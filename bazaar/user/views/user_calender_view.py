from django.views.generic import TemplateView
import datetime as dt
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from django.views import generic
from comp.models import Store,Reservation
class CalenderView(TemplateView):
    template_name = "user/user_calender.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        td = dt.datetime.now()
        today=td.date()
        if year and month and day:
            base_date = dt.date(year=year, month=month, day=day)
        else:
            base_date = today
        store=Store.objects.get(store_id=self.kwargs['pk'])
        # カレンダーは1週間分表示するので、基準日から1週間の日付を作成しておく
        days = [base_date + dt.timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]
        # 9時から17時まで1時間刻み、1週間分の、値がTrueなカレンダーを作る
        calendar = {}
        emp ={}
        for hour in range(store.bussiness_hours_start, store.bussiness_hours_end):
            row = {}
            empty={}
            for day in days:
                r_day=dt.date(year=day.year,month=day.month,day=day.day)
                reserve=Reservation.objects.filter(reservation_hour=hour,reservation_day=str(r_day)).all()
                if reserve=={}:
                   row[day] = True
                   empty[day]=store.seat
                else:
                    ctx=0
                    for reserves in reserve:
                        ctx+=reserves.nop
                    if store.seat <= ctx:
                        row[day] = False
                    else:
                        empty[day]=store.seat-ctx
                        row[day] = True
            calendar[hour] = row
            emp[hour]=empty
        context['calendar'] = calendar
        context['days'] = days
        context['start_day'] = start_day
        context['end_day'] = end_day
        context['before'] = days[0] - dt.timedelta(days=7)
        context['next'] = days[-1] + dt.timedelta(days=1)
        context['today'] = today
        context['empty'] = emp
        context['store']=store
        context['public_holidays'] = settings.PUBLIC_HOLIDAYS
        return context