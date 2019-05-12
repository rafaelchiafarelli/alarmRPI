from omxplayer.player import OMXPlayer
from pathlib import Path
import pygame
from handler import handler

from audio_manager_first_try.settings import ALARM_CONFIG_PATH, MEDIA_ROOT

import time

class player_pygame():
    player = pygame

    
    def __init__(self):
        #player = OMXPlayer
        self.player_list = dict()
        self.player.mixer.init()
        self.player.mixer.music.set_volume(50.0)
        self.this_handler = handler(1,self.player_handler)
        self.this_handler.start()
        
    def player_handler(self):
        #stopped playing now what?
        if self.player.mixer.music.get_busy() == False: #music ended
            #remove the played song from the list
            self.player_list = dict()
            
        
        
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
        self.player.mixer.music.stop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
