from machine import Pin

# +- Blinking using buttons +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

led = Pin(25, Pin.OUT)

button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    led.value(not button.value())



"""
   using not there cause button is initially configured to Pull_Up transistor   
   hence when pressed button.value is gonna be 0 and at rest it is 1. 
"""

           