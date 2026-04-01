# Zero to Pico Hero

This repo is my personal documentation (amature) of building a DIY Guitar Hero controller from scratch using a Raspberry Pi Pico. Since I didn't have much experience with embedded coding, I decided to learn by building it in three different languages: MicroPython, CircuitPython, and C. 

The final goal is to keep the project in C, preferably bare-metal. Python was a great stepping stone to get comfortable with the hardware before diving into the deep end.

## The Journey
I started with MicroPython to quickly get a grasp of how embedded coding works. Being Python, it wasn't hard to learn or get used to.

* **Phase 1: The "Extras"**
    * Before making a prototype, I played around with basic MicroPython scripts and various sensor experiments. You can find these in the `/extras` folder.
* **Phase 2: MicroPython (Serial-over-USB)**
    * I built the initial concept here, including the button logic and debouncing. 
    * One problem I encountered was the lack of native built-in HID support in MicroPython.
    * The workaround i used is serial communication via the `sys` library, but it's a bit tedious to make it work like a proper plug-and-play controller.
* **Phase 3: CircuitPython (Native HID)**
    * This was relatively easy as the existing logic translated well from MicroPython.
    * Using the Adafruit `usb_hid` library made the input part much more practical. By using a custom report descriptor, the Pico tells the computer "I am a standard Gamepad," and it works instantly.
    *  Testing: On Windows, I used the `joy.cpl` command in the Run dialog to verify that the buttons were registering correctly as a gamepad. Same can be used with C versions.
* **Phase 4: C (Bare Metal)**
    * My initial plan was to go straight to bare-metal C, but that is a bit difficult for now.
    * I am currently using the **TinyUSB HID** library as a starting point, and from there, I'll make the jump to bare-metal C.

---

##  Project Structure
```text
/zero-to-pico-hero
├── /C                 # Under progress (TinyUSB/Bare Metal)
├── /micro-python      # Phase 2: Custom bitmask serial reader
├── /circuit-python    # Phase 3: Native HID Gamepad (Final)
├── /extras            # Random Pico experiments & sensor tests
└── /docs              # To be uploaded (Wiring diagrams & project photos)

```

Built as a personal learning project.
