from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from alarm_config.models import Alarm
from landpage.models import  Device
# Create your views here.


#landpage - just connected page - every time someone connects to it, will fall here
    #requires a password (printed in front of the device) to access it
        #password and loggin are the same as the SSID and pswd for the network

#logged in page is a dashboard page
    #on the left panel:
        # the 4 std alarms 
        # create new alarm (up to 4 more)
        # statistics available 
        # contact support
    #on the middle, all the forms will be rendered as the user selects the alarm
    #DO we have a finite number of alarms?
        #I believe we have a standard number of alarms, witch is 4
        #and we can build more up to the input amount

def get_data():
    alarms = Alarm.objects.all()
    device = Device.objects.first() 
    alarmcount = alarms.count()
    img_dev = device.image    
    context = {
        'alarms':alarms,
        'img_dev':img_dev,
        'alarmcount':alarmcount,
        }
    return context

def landpage(request):    
    #alarms
        #each alarm has a name "Alarm #" where, # is the number
    context = get_data()
    return render(request, 'landpage/land.html', context)

@login_required()
def home(request):
    context = {}
    return render(request, 'landpage/home.html', context)


def ContactInfo(request):
    context = {}
    return render(request, 'landpage/contact.html', context)














