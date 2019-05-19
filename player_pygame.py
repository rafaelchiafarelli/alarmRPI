from omxplayer.player import OMXPlayer
from pathlib import Path
import pygame
import threading

from audio_manager_first_try.settings import ALARM_CONFIG_PATH, MEDIA_ROOT

import time

class player_pygame(threading.Thread):
    player = pygame

    
    def __init__(self,name):
        #player = OMXPlayer
        self.player_list = dict()
        self.player.mixer.init()
        self.player.mixer.music.set_volume(50.0)
        threading.Thread.__init__(self)
        self.name = name
        self.die = False

        
    def player_handler(self):
        #stopped playing now what?
        if self.player.mixer.music.get_busy() == False: #music ended
            #remove the played song from the list
            self.player.mixer.quit()            
            self.player_list = dict()
            self.player.mixer.init()
       
    def play_song(self, play_this):
        if not self.player_list:
            self.player_list = play_this
            self.player.mixer.music.load(MEDIA_ROOT+'/'+play_this['audiofile'])
            self.player.mixer.music.play()
        else:
            if play_this['audiofile'] != self.player_list['audiofile']:
                if self.player_list['blocking'] == '0':
                    self.player_list = play_this
                    self.player.mixer.music.load(MEDIA_ROOT+'/'+play_this['audiofile'])
                    print(self.player_list['audiofile'])
                    self.player.mixer.music.play()                        
        return 0

    def stop_song(self):
        #only stops if the signal is configured as continuous. 
        #don't stop otherwise
        if self.player_list:
            if self.player_list['trigger'] == '1':
                self.player.mixer.music.stop()
            
            
    def stop_all(self):
        if self.player_list:
            self.player.mixer.music.stop()
            self.player_list = dict()
            
    def get_playing(self):
        return self.player_list
        
    def run (self):
        while not self.die:
            self.player_handler()
            print('player')
            time.sleep(1)

    def join(self):
        self.die = True
        print("will stop the player")
        self.player.mixer.music.stop()
        super().join() 
                                  
                                     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
