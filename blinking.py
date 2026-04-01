from machine import Pin
import time

# +- Blinking +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

led = Pin(25, Pin.OUT)

while True:
    led.toggle()         # elsewise state as opposed to current state
    time.sleep(1)        # blinks over 1 sec interval
    
    
    
#time.sleep()         pause in seconds
#time.sleep_ms()      pause in milliseconds
#time.sleep_us()      pause in microseconds
#time.ticks_ms()      millisecond timer
    
    