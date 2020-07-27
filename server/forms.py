from django import forms
from .models import *

class HostForm(forms.ModelForm):
    class Meta:
        model= Host_Server
        fields=('name','ip_address','ram','processor','hdd','os','descriptions','status','site','sn')


class VMForm(forms.ModelForm):
    class Meta:
        model= VM_Server
        fields=('name','ip_address','ram','processor','hdd','os','descriptions','app_owner','status','container','dpm')