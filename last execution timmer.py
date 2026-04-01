from machine import Pin
import time

# +- Last Execution Timmer +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-


led = Pin(25, Pin.OUT)

last = time.ticks_ms()        # the time in milliseconds since the Pico started

while True:
    if time.ticks_diff(time.ticks_ms(), last) > 500:   # if 500ms have passed since last state change only then will code below be executed 
        led.toggle()
        last = time.ticks_ms()
        
        

"""
note: in micropython the time module stores/measure time in float data type hence we cant         
just take difference of it to compare or set condtions we MUST use ticks.diff(end-time,start-time)
this helps avoid wrap back cause of floats hence keeping result true if an overflow does accur.   

"""


