from django.db import models
from .gpio_reference import gpio_mode_choices, alarm_mode, blocking_mode, availalbe_gpios
import os

# Create your models here.

class Trigger(models.Model):
    #one specific GPIO
    #one mode (while pressed, if pulsed)
    def __str__(self):
        return models.Model.__str__(self)

    
class Alarm(models.Model):
    #trigger
       
    trigger = models.CharField(max_length=100, 
        choices=gpio_mode_choices, 
        default = 'pulso',
        blank = False,
        null = False)
    #gpio_reference
    
    gpio_number = models.CharField(max_length=100, 
        choices=availalbe_gpios, 
        default = 'canal 1',
        blank = False,
        null = False)
    #blocker
    blocking = models.CharField(max_length=100, 
        choices=blocking_mode, 
        default = 'bloqueador',
        blank = False,
        null = False)
    
    #audiofile
    audiofile = models.FileField(upload_to='media/',blank = True,
        null = True)
    uploadedat = models.DateTimeField(auto_now_add=True,blank = True,
        null = True)
    
    def __str__(self):
        return models.Model.__str__(self)
        