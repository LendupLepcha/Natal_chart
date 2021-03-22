from django import forms
from . import models

class TakeInput(forms.ModelForm):
    class Meta:
        model = models.User_info
        fields = ['name','year', 'month', 'day', 'hour', 'minute', 'latitude', 'longitude']
class Search_Input(forms.Form):
    # sname = forms.CharField( max_length=100)
    syear = forms.IntegerField()
    smonth = forms.IntegerField()
    sday = forms.IntegerField()
    shour = forms.IntegerField()
    sminute = forms.IntegerField()
    slatitude = forms.FloatField()
    slongitude = forms.FloatField()
