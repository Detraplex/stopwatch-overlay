# Intro - timer and stopwatch
built with 100% tkinter and python, this project looks to be used for streamers who dont want to use a google timer or Snaz because its confusing and dumb.
# Use
when using OBS or Streamlabs add a window capture, change the window match prioritiy to __Window title must match__ and deselect capture cursor.
# Known issues and the future
so far we do not have a dependencies file and automatic installer, i am looking at adding a more robust GUI, or a double window app, honestly not to sure right now. if you do not have Tkinter installed that will be an automatic issue, beides that there is also an issue when useing the starting soon button, it will initalize and then try to go back and countdown or up. ill fix that when i have time. it also open up a command promt and it will break if the time isn't formatted correctly when using the timer function -> 00:00:00:0000.