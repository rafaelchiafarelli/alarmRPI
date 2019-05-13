from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import DetailView, UpdateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from alarm_config.models import Alarm
from django.forms.widgets import FileInput
from django.contrib.admin.utils import help_text_for_field
from django.conf import settings
import json
from audio_manager_first_try.settings import ALARM_CONFIG_PATH

class AlarmUpdateForm(forms.ModelForm):

    class Meta:
        model = Alarm
        fields =(
                'trigger',   
                'gpio_number',
                'blocking',  
                'audiofile', 
                )
        labels = {
                'trigger':'Disparo por',
                'gpio_number':'Contato',
                'blocking':'Bloqueia?',
                'audiofile':'Arduivo Atual',
                }
        widget = {'audiofile':forms.FileInput()}
        formfield_overrides = {
                    Alarm.audiofile: {'widget': forms.FileInput },
                    }
    def SaveToJson(self,this_id):
        print("will save the f....ing file!")
        d = self.cleaned_data
        print(d)
        tmp=d['audiofile'].__str__()
        d['audiofile'] = tmp
        path = ALARM_CONFIG_PATH
        file = path+'config' + this_id.__str__() + '.json'
        with open(file,'w') as outpufile:
            json.dump(d,outpufile)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AlarmCreateForm(forms.ModelForm):
    class Meta:
        model = Alarm
        fields =(
            'trigger',   
            'gpio_number',
            'blocking',  
            'audiofile', 
            )
        labels = {
                'trigger':'Disparo por',
                'gpio_number':'Contato',
                'blocking':'Bloqueia?',
                'audiofile':'Arduivo',
                }
        
        widget = {'audiofile':forms.FileInput()}
        formfield_overrides = {
                    Alarm.audiofile: {'widget': forms.FileInput },
                    }
    def SaveToJson(self,this_id):
        print("will save the f....ing file!")
        d = self.cleaned_data
        print(d)
        tmp=d['audiofile'].__str__()
        d['audiofile'] = tmp
        path = ALARM_CONFIG_PATH
        file = path+'config' + this_id.__str__() + '.json'
        with open(file,'w') as outpufile:
            json.dump(d,outpufile)
        
        
        
    def form_valid(self, model):
        model.instance.user = self.request.user
        return super(AlarmCreateForm, self).form_valid(model)
    
    
    
    
    