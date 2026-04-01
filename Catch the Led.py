import digitalio
import board
import time
import random


led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP



print("Get ready... Press the button when the LED turns on!")

while True:
    led.value = False
    time.sleep(random.uniform(2, 5))  # Random delay before LED turns on
    led.value = True
    start_time = time.monotonic()

    while button.value:  # Button not pressed
    # pass forces repetition on this while loop until button is pressed(0/flase)
        pass             

    reaction_time = time.monotonic() - start_time
    led.value = False         

# +- Difficulty togle +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    
    if reaction_time < 3:
        print(f"Caught! Total reaction time: {reaction_time:.3f} seconds")
    else:
        print(f"Too slow! Your reaction time: {reaction_time:.3f} seconds")
    
    time.sleep(3)  # Short pause before next round(no exit yet)
    #TODO make a exit condtion for the game 


