import time
def countdown(time_sec):
    while time_secs:
        mins,secs=divmod(time_sec,60)
        timeformat='{:02d}:{:02d}'.format(mins,secs_)
        print(timeformat)