from django.urls import path
from .views import UpdateAlarm, CreateAlarm,Success


urlpatterns = [
    path('alarms/<int:pk>', UpdateAlarm, name='update'),
    path('alarms/Create', CreateAlarm, name='create'),
    path('alarms/success',Success,name='success'),
    path('alarms/fail',Success,name='fail'),
    ]