import multiprocessing

bind = 'unix:/home/pi/alarmRPI/alarmRPI.sock'
workers = multiprocessing.cpu_count() * 2 + 1
reload = True
daemon = True
