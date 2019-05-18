from audio_manager_first_try.settings import ALARM_CONFIG_PATH, MEDIA_ROOT

from player_pygame import player_pygame
from gpio_module import gpio_module

import os
import json

class MainClass():
    player = player_pygame()
    signals = gpio_module()
    signals.config()

    #alarms with "blocking = 1" will have priority
    #priority between alarms with blocking = 1 is "the newer the prior" 
    #that means that, if any alarm was created last, has priority 
    def list_and_organize(self):
        files_list = os.listdir(ALARM_CONFIG_PATH) #get all the config files from the system
        data = list() #initialize the list return list
        for file in files_list:
            complete_path = os.path.join(ALARM_CONFIG_PATH, file) 
            with open(complete_path) as json_file:
                current_data=json.load(json_file)
                if current_data['blocking'] == '0':
                    data.append(current_data)
                else:
                    data.insert(0,current_data)
        return data
    
        
  
    #current_config are a list of available configurations 
    def logic(self,current_config):
        if current_config: #it is correctly configured
            off_signal_count = 0
            for alarm_enum in range(0,9): ##each signal must be verified
                current_signal = self.signals.get_input(alarm_enum)
                if alarm_enum == 0:
                    #emergancy signal
                    if current_signal[0] == 'on': #the mute signal was triggered
                        self.player.stop_all()
                else:
                    if current_signal[0] == 'on': #this signal was triggered
                        for config in current_config:
                            #check each configured alarm
                             if alarm_enum.__str__() == config['gpio_number']:  #if signal correspond to an alarm
                                if current_signal[1] == 'continuous' and config['trigger'] == '1':
                                    #alarm trigered with the specified signal type, run the alarm
                                    self.player.play_song(play_this=config)
                                if current_signal[1] == 'pulsed' and config['trigger'] == '0':
                                    #alarm trigered with the specified signal type, run the alarm
                                    self.player.play_song(play_this=config)
                    else:
                        off_signal_count+=1 #count the signals that are off to turn all songs off afer
            if off_signal_count == 9:
                self.player.stop_song()
                               
                                                 

                                
                                
                                
                                
                                
                                
                                
                                
                                
                              