from adafruit_clue import clue
from time import sleep


# declaring a varible wherein I put the title, color and text-scale
clue_display = clue.simple_text_display(title="Message Streamer", title_color=(clue.RED),  text_scale=2,)
# I make three variables and initializing it in assigning a String value in each variable
message = "This message moves from right to left"
message2 = "This message moves from left to right"
message3 = "This message blinks"
while True: 
   clue_display[1].text = message          #assigning the text in the second line with the value of message
   clue_display[1].color = clue.YELLOW     # assigning the color of the value message with yellow
   #this displays the value of message from right to left with the use of the slice notation in python
   # items start in index 1 and continue to the rest of an array and concatenate it with the message starts
   message = message[1:] + message[0:1]    # with index 0 and stops in index 1
                    
   clue_display[3].text = message2          #assigning the value of message2 in the clue_display of the index 3 
   clue_display[3].color = clue.WHITE       #assigning the color of the value of message2 to white
   sleep(.3)                                #sleeps in .3 seconds
   #this makes the message move from left to right          
   move =  message2[len(message2) - 1]      #store the result of this code in move varible 
   message2 = move + message2[:-1]          #where the lenght of the message2 minus 1
   #this makes the message blinks
   clue_display[5].text = message3          #assign the clue_display with the value of message3
   clue_display[5].color = clue.SKY         #assign the color of the message3 to sky
   sleep(1)                                 #sleep in 1 second
   clue_display[5].color = clue.BLACK       #set the color of the message3 to black to make the result blinking
   clue_display.show()                      #show result

  