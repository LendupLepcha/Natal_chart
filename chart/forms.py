from django import forms
from . import models

class TakeInput(forms.ModelForm):
    class Meta:
        model = models.User_info
        fields = ['year', 'month', 'day', 'hour', 'minute', 'latitude', 'longitude']
