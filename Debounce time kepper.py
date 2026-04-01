from machine import Pin
import time



button = Pin(15, Pin.IN, Pin.PULL_UP)   
led    = Pin(25, Pin.OUT)

# +- Debounce Logic +-+-+-+-+-

Debounce_ms = 20
stable_state = 1
suspect_state = 1            # 1 is off, 0 is onn/pressed due to Pull-up
susp_time = 0

def is_button_toggled():
    global stable_state, suspect_state, susp_time
    
    now_time = time.ticks_ms()
    raw = button.value()
    toggled = False                                                 

    if raw != suspect_state:
        suspect_state = raw
        susp_time = now_time
        
    elif time.ticks_diff(now_time, susp_time) >= Debounce_ms:         # cheking stability over 20ms , cant do normal subtraction cause of value type of time/utime .ticks_ms in micro py
        if raw != stable_state:
            if raw == 0:                                              # falling edge (pressed)
                toggled = True
            stable_state = raw

    return toggled



# +- Main loop +-+-+-+-+-

while True:
    if is_button_toggled():
        led.toggle()
    time.sleep_ms(5)

"""
not the best example to test on led as even if there is debounce it wont be noiced easily
but still it works (hopefully)

"""