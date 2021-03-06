import RPi.GPIO as gpio
import time
import threading
from handler import handler

class gpio_module(threading.Thread):
    available_inputs = list()
    die = False    
    available_inputs = {0:4, 
                        1:17,
                        2:27,
                        3:22,
                        4:5,
                        5:6,
                        6:13,
                        7:26,
                        8:18,
                         }
    #checking pulsed continuous
    current_state = {0:['off','continuous',0],
                     1:['off','continuous',0],
                     2:['off','continuous',0],
                     3:['off','continuous',0],
                     4:['off','continuous',0],
                     5:['off','continuous',0],
                     6:['off','continuous',0],
                     7:['off','continuous',0],
                     8:['off','continuous',0],
                    }

    def __init__(self, name):
        self.config()
        threading.Thread.__init__(self)
        self.name = name

    def continuous_update(self):
        #check all inputs and update the module variables
        for num  in range(len(self.available_inputs)):
            if gpio.input(self.available_inputs[num]) == 1:
                #pulled up, so check for how long it is up
                if self.current_state[num][1] == 'pulsed':
                    self.current_state[num][2] -= 1
                    if self.current_state[num][2] == 0:
                        self.current_state[num] = ['off','continuous',0]
                else:
                    if self.current_state[num][1] == 'checking':
                        if self.current_state[num][2]>7 and self.current_state[num][2]<16:
                            self.current_state[num] = ['on','pulsed',100]
                        else: 
                            self.current_state[num] = ['off','continuous',0]
                    else:
                        self.current_state[num] = ['off','continuous',0]
                
            else:
                if self.current_state[num][0] == 'off' and self.current_state[num][1] == 'continuous':
                    self.current_state[num] = ['off','checking',0]
                                        
                if self.current_state[num][1] == 'checking':
                    self.current_state[num][2] += 1
                    print(self.current_state[num][2])
                    if self.current_state[num][2] >  20:
                        self.current_state[num] = ['on','continuous',0]
                    
                    
                

    def config(self):
        gpio.cleanup()
        gpio.setmode(gpio.BCM)
        for num  in range(len(self.available_inputs)):
            gpio.setup(self.available_inputs[num],
                       gpio.IN, 
                       pull_up_down=gpio.PUD_UP)
           # gpio.add_event_detect(self.available_inputs[num],
           #                       gpio.BOTH,
           #                       callback = self.callback_change,
           #                       bouncetime=50)

    
    def closeup(self):
        gpio.cleanup()
        
    def get_input(self,signal):
        #return format {'signal':'3', 'type':'1'}
 #       ret = {'signal':signal.__str__(),'type':'0'}
 #       if self.current_state[signal][0] == 'on':
 #           ret = {'signal':signal.__str__(),'type':'1'}        
        return self.current_state[signal]
#        return ret

    def run (self):
        while not self.die:
            self.continuous_update()
            time.sleep(0.025)

    def join(self):
        self.die = True
        print("will close the gpio module")
        self.closeup()
        super().join()
        

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        