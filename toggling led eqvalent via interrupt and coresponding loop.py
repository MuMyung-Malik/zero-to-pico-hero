from machine import Pin

# +- Interrupts for led GP 25 with button  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

led = Pin(25, Pin.OUT)

button = Pin(15, Pin.IN, Pin.PULL_UP)

def pressed(pin):
    led.toggle()
    print("Button pressed, led is toggled.")

button.irq(trigger=Pin.IRQ_FALLING, handler=pressed)


# +- intrupt alternate using Loop for led GP 25 with button +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

led = Pin(25, Pin.OUT)

button = Pin(15, Pin.IN, Pin.PULL_UP)

if button.value() == 1:
    led.toggle()
    print("Button pressed led is toggled.")


"""
 the reason why intrupts are used instead of some eqvalent loop is because
 loops cost more in terms of cpu usage are they keep polling for check    
 againsts the set conditon but interrupts can run on minimal cpu costs    
 keeping it efficient and more ideal.                                     
 

 though it does complicates it a lil bit

"""


 