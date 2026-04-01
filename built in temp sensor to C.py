from machine import ADC
import time

sensor = ADC(4)                                 # DEFINES sensor as the built in temp sensor

conversion_factor = 3.3 / 65535                 # converts adc reading into voltage by dividing the 3.3V to 65535 (16 bit reading?)

while True:
    reading = sensor.read_u16() * conversion_factor        # from datasheet (0.706V is reference for pico at 27C)	
    temperature = 27 - (reading - 0.706) / 0.001721
    print("Temperature:", temperature, "°C")
    time.sleep(1)