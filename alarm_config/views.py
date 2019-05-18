from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from alarm_config.models import Alarm

from alarm_config.Forms import AlarmUpdateForm, AlarmCreateForm

from landpage.views import get_data

# Create your views here.

# Create your views here.
@login_required()
def UpdateAlarm(request, pk=None):
    obj = get_object_or_404(Alarm, pk=pk)
    form = AlarmUpdateForm(request.POST or None, request.FILES or None,instance = obj)
    context = get_data()
    context = dict(context,**{'form':form})
    context = dict(context,**{'file':obj.audiofile})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form.SaveToJson(obj.id)
        return redirect('/alarms/success')
    return render(request, 'alarm_config/update.html',context)

@login_required()
def CreateAlarm(request):
    context = get_data()    
    if request.method == 'POST':
        form = AlarmCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form.SaveToJson(Alarm.objects.last().id)
            return redirect('/alarms/success')
        else:
            return redirect('/alarms/fail')
        
    form = AlarmCreateForm()    
    context = dict(context,**{'form':form})        
    return render(request, 'alarm_config/create.html', context)

def Success(request):
    context = get_data()
    return render(request,'alarm_config/success.html',context)

def Fail(request):
    context = get_data()
    return render(request,'alarm_config/fail.html',context)
