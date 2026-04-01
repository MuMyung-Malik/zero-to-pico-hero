# Pico Playground & Experiments

This folder contains the random experiments I did while getting used to the Raspberry Pi Pico. Most of these are written in MicroPython. These scripts helped me get used to coding on the Pico, understanding how to read inputs and handle timing before I applied those concepts to the Guitar Hero project.

## File List (I'll omit the basic ones here and only mention the most interesting ones)

* `built in temp sensor to C.py`: Reads data from the onboard temperature sensor and outputs in Degrees Celsius. Works on a fascinating voltage-to-temperature conversion logic.
* `Catch the Led.py`: This is a simple reaction-time game built in CircuitPython. It uses the built-in LED and an external attached button. It's unpolished in the sense of a proper game, but a good concept and practice component.
* `current time and day.py`: Experimenting with the RTC (Real-Time Clock) module. It's fascinating how the Pico can keep track of time.
* `Debounce time kepper.py`: After testing different methods for handling mechanical button bounce, this stood out to me the most as it isn't too complex but gets the job done, especially for my small-scale project.
* `sys module.py`: Exploring the functionality of the `sys` module. This was such a eureka moment when I discovered the sys module being used as a debugging method. Though a pain in the neck in my case alas... but still cool.
* `toggling led eqvalent via interrupt and corespon...`: Interrupts are a cool concept and an alternative to loops as they aren't power intensive, but I might not use them as they tend to get complex.

---

*Part of the Zero to Pico Hero journey.*
