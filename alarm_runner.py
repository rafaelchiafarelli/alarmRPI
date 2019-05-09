from audio_manager_first_try.settings import ALARM_CONFIG_PATH, MEDIA_ROOT
import os
import json
from alarm_config.gpio_reference import blocking_mode
from django.utils.functional import empty

from AlarmMainClass import MainClass

      
    
if __name__ == '__main__':
    import time
    run_count = 0
    m = MainClass()
    while True:
        now_playing=list()
        file = open('/home/rafael/django-workspace/audio_manager_first_try/test_file.txt','a+')
        file.write("hello motherfuckers\r\n")
        file.close()

        #list all alarms available
        #check GPIO status
        #play alarms according to it's logic
        
        #list all alarms available
            #remove alarms with no audio files attached to it
            #put all blocking alarms in the beginning of the list
        organized_list_of_alarms = m.list_and_organize()  
        #GPIO - abstracted for now
            #active or not active
            #is a pulse or continuous
            #update the current state
        if run_count == 0:
            MOC_gpio_signal = list()
            MOC_signal = {'signal':'3', 'type':'1'}
            MOC_gpio_signal.append(MOC_signal)
            MOC_signal = {'signal':'2', 'type':'1'}
            MOC_gpio_signal.append(MOC_signal)
            MOC_signal = {'signal':'3', 'type':'0'}
            MOC_gpio_signal.append(MOC_signal)
            MOC_signal = {'signal':'4', 'type':'0'}
            MOC_gpio_signal.append(MOC_signal)
            MOC_signal = {'signal':'5', 'type':'1'}
            MOC_gpio_signal.append(MOC_signal)
        if run_count == 10:
            MOC_gpio_signal = list()
            MOC_signal = {'signal':'3', 'type':'1'}
            MOC_gpio_signal.append(MOC_signal)
            MOC_signal = {'signal':'2', 'type':'1'}
            MOC_gpio_signal.append(MOC_signal)
            MOC_signal = {'signal':'1', 'type':'1'}
            MOC_gpio_signal.append(MOC_signal)
            MOC_signal = {'signal':'4', 'type':'0'}
            MOC_gpio_signal.append(MOC_signal)
            MOC_signal = {'signal':'5', 'type':'0'}
            MOC_gpio_signal.append(MOC_signal)
            
        run_count +=1
        #logic
            #if alarm has audio 
            #signal
            #signal type (pulse or continuous)
            #blocking
            #launch alarm 
        print("will run the logic with current_config")
        print(organized_list_of_alarms)
        print("will run the logic with current_signals")
        print(MOC_gpio_signal)
        print('now playing these songs')
        print(now_playing)
        m.logic(current_config=organized_list_of_alarms,current_signals=MOC_gpio_signal,now_playing=now_playing)
        time.sleep(1)
        
        
        
        
        
        
        
        
        
        
        