from django import forms

stars_list = [('1','星１'),('2','星２'),('3','星３'),('4','星４'),('5','星５')]

class KutikomiForm(forms.Form):
    stars = forms.CharField(label="評価",required=True,widget=forms.RadioSelect)
    impressions = forms.CharField(label="感想",required=True)