"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""
from microbit import *
from time import sleep

while True:
    for y in range (5):        #loop for the index belongs to y
        for x in range(5):     #loop for the index belongs to x
            display.set_pixel(x,y,9)  #Set the brightness of the LED at column x and row y to value, which has to be an integer between 0 and 9.
            sleep(.5)         #Set the time duration of the lights               
            display.clear()   # Set the brightness of all LEDs to 0 (off).

   