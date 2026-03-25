"""
Created by: Illia
Created on: March 24
This module is a Micro:bit MicroPython program
"""

from microbit import *
import neopixel

lightlevel = 0
np = neopixel.NeoPixel(pin16, 4)

display.clear()

# initialize all pixels to black
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np[3] = (0, 0, 0)
np.show()

display.show(Image.HAPPY)

while True:
    if button_a.was_pressed():

        # light level
        lightlevel = display.read_light_level()
        display.scroll(str(lightlevel))

        # 0 neopixels
        if lightlevel <= 51:
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
            np.show()

        # 1 neopixel
        if lightlevel > 52:
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
            np[0] = (255, 255, 255)  # white
            np.show()

        # 2 neopixels
        if lightlevel > 104:
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
            np[1] = (0, 255, 0)  # green
            np.show()

        # 3 neopixels
        if lightlevel > 156:
            np[3] = (0, 0, 0)
            np[2] = (255, 0, 0)  # red
            np.show()

        # 4 neopixels
        if lightlevel > 208:
            np[3] = (0, 0, 255)  # blue
            np.show()
