from audio_manager_first_try.settings import ALARM_CONFIG_PATH, MEDIA_ROOT

from player_omx import player_omx
import os
import json


class MainClass():
    player = player_omx()
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
    
        
    #current_signals are a list of available signals fired
    #current_config are a list of available configurations 
    def logic(self,current_config,current_signals,now_playing):
        #print('inside logic')
        if current_signals:
         #   print('has signals')
            if current_config:
          #      print('has config')
                for signal in current_signals:
           #         print('current signal')
            #        print(signal)
                    for config in current_config:
             #           print('current config')
              #          print(config)
                        if signal['signal'] == config['gpio_number']:
               #             print("play/pause the alarm set to it") 
                            if signal['type'] == config['trigger']:
                #                print('audio file is')                                
                 #               print(config['audiofile'])
                                self.player.play_song(play_this=config)
                            #else:
                  #              print('wrong signal')
                                
                                
                                
                                
                                
                                
                                
                                
                                
                              