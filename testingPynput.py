# I've successfully used pynput to make a timer. Shoutout to 'reading the documentation' for getting me there. 
# Currently this program does exactly what I want it to do, with one caveot:
# I don't know what type of input the arcade machine controls will register as. 
# Controls will arrive shortly. If by some miracle, pynput picks it up as a keyboard, this program will work. 
# That's incredibly unlikely though, so I'll probably have to figure out how to use general USB activity instead
# of keyboard input. 

from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

virtualkeyboard = Controller()

timer = 1800
randomnumber = 3        #I know it's not random. That's over my head right now

while True: #loops the whole thing

    if timer >= 1: #runs if the timer hasn't yet run out

        # The event listener will be running in this block
        with keyboard.Events() as events:
            # Block at most one second
            event = events.get(1.0)
            if event is None:             #if a key isn't pressed in 1 second, lower the timer by 1
                timer = (timer - 1)
                # print('timer is',timer)   #placeholder for me to see what's happening
            else:
                timer = 1800              #if a key is pressed, reset the timer
                # print ('keypress')        # and print for me to see what's happening
                
    else:                                  #if the timer runs out, this runs
        virtualkeyboard.press(Key.esc)     #exits out of game
        virtualkeyboard.release(Key.esc)
        time.sleep(2)
        
        for i in range(int(randomnumber)):  #scrolls down between 3 and 6 times
            virtualkeyboard.press(Key.down)
            virtualkeyboard.release(Key.down)
            time.sleep(1)                     #waits one second between each push
            
        virtualkeyboard.press(Key.enter)      #presses enter to open game
        virtualkeyboard.release(key.enter)
        time.sleep(1)
        
        randomnumber = (randomnumber + 1)    #increases amount of scrolls by 1
        
        if randomnumber > 6:             #if scrolls exceeds 6, make it 3
            randomnumber = 3
            
        else:
            continue                 #exit if/then 
        
        
        timer = 3400               #wait an hour ish before doing it again
        continue                  # keep on looping
