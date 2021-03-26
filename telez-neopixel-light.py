"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
from adafruit_circuitplayground import cp
from time import sleep

temporary = 32      #temporay is used for floor division to get the neopixel color and its specific color
color = 0          #this is for the increasing color  using light sensor
indx = 0            # indx is referring to the index 0-9
glow_point = 0      #intializes glow_point as beginning glowing point

while True:

    indx = cp.light // temporary       # this is used to get the neopixel index
    glow_point = indx * 32             # this is used in controlling the brightness of the neopixel
    color = 255 * (cp.light - glow_point) // temporary   # in this variable will stored the result of the executed condition and detect what brightness it should be 
    
    for i in range(10):                     #this is the loop for 0-9 pixels    
        if i < indx:                        #if i is less than to the neopiexel indx 
            cp.pixels[i] = (000, 255, 255)  #the pixels will glow
        if i > indx:                        # if i is greater than neopixel index 
            cp.pixels[i] = (0, 0, 0)        # the neopixels glow sleeps 
        if indx > 9:                        #if indx is greater than 9
            cp.pixels[9] = (000, 255, 255)  #the neopixel 9 glows
        else:
            cp.pixels[indx] = (color, color, color) # it will executes to fill all the color accordingly
            

   

