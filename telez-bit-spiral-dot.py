"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from time import sleep


ledpattern = [                                                  #this array convey the led light patterns   
               [0,0],[1,0],[2,0],[3,0],[4,0], 
               [4,1],[4,2],[4,3],[4,4],[3,4],
               [2,4],[1,4],[0,4],[0,3],[0,2],
               [0,1],[1,1],[2,1],[3,1],[3,2],
               [3,3],[2,3],[1,3],[1,2],[2,2]
              ]
while True:
    for i in range(0,len(ledpattern)):                          #check the lengths of an array
        display.set_pixel(ledpattern[i][0], ledpattern[i][1],9) #set the brithness of led light
        sleep(0.5)                                              #set the time duration of the led brightness
        display.set_pixel(ledpattern[i][0], ledpattern[i][1],0) #turn off all the led lights
