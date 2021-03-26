"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
from time import sleep, time
from random import randint 

clue_display = clue.simple_text_display(title="REACTION GAME", title_color=(clue.YELLOW),  text_scale=2,)


while True:
    clue_display[0].text = "Instructions:"         #this displays the instructions 
    clue_display[0].color = clue.GREEN             #for the game
    clue_display[1].text = "Player 1 press A"
    clue_display[1].color = clue.WHITE
    clue_display[2].text = "Player 2 press B"
    clue_display[2].color = clue.WHITE
    clue_display[3].text = "Press if the number"
    clue_display[3].color = clue.SKY
    clue_display[4].text = "is divisible by 2"
    clue_display[4].color = clue.SKY
    clue_display[5].text = "Maximum score of 5"
    clue_display[5].color = clue.YELLOW
    
   
    for i in range (5, 0, -1):                        #this displays the starting time 
        clue_display[6].text = "Starts in " + str(i)  #for the game
        clue_display[6] .color = clue.RED
        sleep(1)                                       #time duration of the text to display
        clue_display[6].color =clue.BLACK              #setting the color of index 6 to black makes
                                                       #text blinks

        A_score = 0                                    #this is a variable for storing the score of player A
        B_score = 0                                    #this is a variable for storing the score of player B
      
        if i == 1:
            while True:
                num =  randint(1, 100)                  #variable num stores the random number of 1 - 100
                clue_display[0].text = ""               #empty the text for line spacing
                clue_display[1].text = ""               
                clue_display[2].text = "" 
                clue_display[3].text = ""
                clue_display[4].text = "Player A score: " + str(A_score) #in index 4 displays the text and the player's A score 
                clue_display[5].text = "Player B score: " + str(B_score) #in index 5 displays the text and the player's B score
                clue_display[6].text = ""

                clue_display[1].text = "        " + str(num)              #in index 1 displays the result of random number
            
                time1 = time()                                         #time1 for player 1
                time2 = time()                                         #time2 for player2
                counter = 1

                while counter > 0:                                     #condition
                    if time2 - time1 >= 1:                             #this condition is for time of both player
                        counter = 0
                    else:
                        time2 = time()      
                    
                    if clue.button_a:                 #this is for the button_a, when letter A is click and
                        if num % 2 == 0:              #if num or the result of random num is modulo 2 equal 0
                            A_score +=1               #the score of Player is A is added by 1
                        else: 
                            A_score -=1               #if not minus 1         
                        break

                    if clue.button_b:                 #this is for the button_b, when letter B is click and
                        if num % 2 == 0:              #if num is modulo 2 equal to 0
                            B_score +=1               #the score of Player B is added by 1
                        else:
                            B_score -=1               #if not, minus 1
                        break
            
                if A_score == 5:                      #if the score of Player A is equal to 5
                    clue_display[1].text = ""         
                    clue_display[1].text = "PLAYER A WINS!" #displays this text
                    clue_display[1].color = clue.RED        #set the color of this text to red
                    break
                        
                    
                if B_score == 5:                             #if the score of Player B is equal to 5
                    clue_display[1].text = ""                
                    clue_display[1].text = "PLAYER B WINS!"  #displays this text
                    clue_display[1].color = clue.RED         #set the color of this text to RED
                    break
                       
            sleep(1)    #time duration
        clue_display.show()
   