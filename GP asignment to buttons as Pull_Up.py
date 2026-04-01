import machine


# +- Button setup +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

button = Pin(5, Pin.IN, Pin.PULL_UP)        # assigns GP 5 to button as pull up

if button.value() == 1:
    print ("button is pressed")




# +- Easier Buttons setups +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

"""

 for mutilple consective GP buttons can also do this 

for i in range (2, 15):
    buttons = Pin(i, Pin.IN, Pin.PULL_UP)                            # defines GP2-GP7 as buttons

 same thing using comprehensive for loop

buttons = [Pin(i, Pin.IN, Pin.PULL_UP) for i in range (2, 15)]      # defines GP2-GP7 as buttons


"""



