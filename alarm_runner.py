from audio_manager_first_try.settings import ALARM_CONFIG_PATH, MEDIA_ROOT
import os
import json
from alarm_config.gpio_reference import blocking_mode
from django.utils.functional import empty

from AlarmMainClass import MainClass



    
    
if __name__ == '__main__':
    import time
    m = MainClass()

    while True:
        
        
        #list all alarms available
            #remove alarms with no audio files attached to it
            #put all blocking alarms in the beginning of the list        
        list_of_alarms = m.list_and_organize()  
        
        #GPIO - low level handler
            #active or not active
            #is a pulse or continuous
            #update the current state
                 #check GPIO status

            
        #play alarms according to it's logic
                
        #logic
            #if alarm has audio 
            #signal
            #signal type (pulse or continuous)
            #blocking
            #launch alarm 
        #print("will run the logic with current_config")
        #print(list_of_alarms)
        m.logic(current_config=list_of_alarms)
        print("this is a print log")
        time.sleep(1)
        
        
        
        
        
        
        
        
        
        
        
