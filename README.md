# more_attractive_mode
A simple Python script to make a retropie arcade automatically switch between games at a fixed interval. 

Currently this is nothing. I know very little python and my goal is to learn some with this very simple project. 

I'm putting together a Retropie arcade cabinet which will use the "Attract Mode" frontend. Contrary to the name, as far as I can tell, Attract mode is only a frontend and nothing else, meaning it won't do anything unless the user makes it do something. I'd like to leave my machine running like a real arcade machine, but I don't want it to sit on the menu screen all the time for fear of screen burn in, and because that's pretty boring. 

The goal of this project is to write a simple script that starts with Retropie and detects user input, or lack thereof. Once it detects that there's been no activity for a set amount of time (I'm thinking 30 minutes), it uses Pynput to simply press 'esc' to get back into the menu if it's in a game, then press the 'up' or 'down' arrow a few times, and finally press 'enter' to load into a game. 

My cabinet will only be running MAME games, so this will load up the arcade game to the title screen, which usually will have its own demo or video to play. Then, after another interval (ideally 1 hour, but it might be 30 minutes as well to keep it simple), it'll do it again. And again. And again. Until it detects user input. At which point the timer will reset every time the user interacts with the machine, so as to avoid the machine kicking you out of a game while playing. 

This is a very simple project, and I don't know much. I'm trying to learn here, so don't yell at me please. 
