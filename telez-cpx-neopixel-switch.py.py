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


  #Default switch is false
neopixels = 9  # How many neopixels are there.
while True:
    cp.pixels[neopixels] = (000, 255, 255)   #Turn the lights on
    sleep(0.5)     #This is the counting of how long the lights on
    cp.pixels[neopixels] = (000,000,000)   # This will turn off the lights after it turns on

    if cp.switch:#True
        neopixels+= 1 # If the switch will click it turns true and increment the neopixels' lights (from 0,1,2,3 and so on.)
    else:#False
        neopixels-=1   # The neopixels'lights will turns on directly because the default settings is False and it will decrement the lights(from 9,8,7, 6 and so on.), it will be true if the switch is click.
    if neopixels <0:  #If neopixels'lights is less than zero ,
        neopixels = 9  #Set lights back to 9.
    elif neopixels >9: # If the neopixels' lights is greater than 9,
        neopixels = 0  #Set back the lights to index 0.
        