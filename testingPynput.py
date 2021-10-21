# The goal here is to understand how pynput detects inputs and figure out how I can use that to make a timer. 
# Currently I'm trying to get it to simply change variable a from 1 to 2 when a key is pressed, and have it 
# print that every second so that I can see it working. Once it does that properly, then I'll worry
# about making it do something useful instead of just changing a variable
#
# ... but right now it doesn't work properly and I'm not sure how to make it work properly...

import time

global a
a = 1

def main():
    
    from pynput import keyboard

    def on_press(key): #this is supposed to change variable a from 1 to 2 when a key is pressed
        global a
        a = 2

    def on_release(key): #it wouldn't let me run this without defining a release, and so 'pass' lets it run
        pass

while True: #loops the program over and over while printing out the value of a every second
    main()
    print('a =',a)
    time.sleep(1)

# Collect events until released
with keyboard.Listener( #listener stuff that I copied and pasted from the example that I found from pynput
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
