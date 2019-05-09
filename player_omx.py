from omxplayer.player import OMXPlayer
from pathlib import Path

from audio_manager_first_try.settings import ALARM_CONFIG_PATH, MEDIA_ROOT

import time

class player_omx():
    player = subprocess.Popen(["mplayer", "", "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    player_list = dict()
    passage_count = 0
    def play_song(self, play_this):
        print('******************')
        print(self.passage_count)
        self.passage_count +=1
        if not self.player_list:
            print('nothing on list, so lets play something')
            self.player.stdin.write("q")
            self.player = subprocess.Popen(["mplayer", MEDIA_ROOT+'/'+play_this['audiofile'], "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.player_list = play_this
        else:
            print('is playing somthing, so better check if we can replace it... :-)')
            if play_this['audiofile'] != self.player_list['audiofile']:
                print(play_this)
                print(self.player_list)
                print('file is not the same')
                if play_this['blocking'] == '0':
                    print('uhuuu lets stop it!')
                    if self.player_list['blocking'] == '0':
                        print('no blocking, change the file')
                        print('change file')
                        self.player.stdin.write("q")
                        
                        self.player = subprocess.Popen(["mplayer", MEDIA_ROOT+'/'+play_this['audiofile'], "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        self.player_list = play_this
                        
                else:
                    print('well, not so lucky... ')
            else:
                print('file is the same... so no change')
        return 0
    def stop_song(self):
        self.player.stop()