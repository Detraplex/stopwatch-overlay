# Intro - timer and stopwatch
built with 100% tkinter and python, this project looks to be used for streamers who dont want to use a google timer or Snaz because its confusing and dumb.
# Use
when using OBS or Streamlabs add a window capture, change the window match prioritiy to `__Window title must match__` and deselect capture cursor. On statup make sure to run `__pip install -r --upgrade-pip__` in a command terminal (`cd <file install path>Win+r cmd + enter`). Tkinter is a built in lib so we dont have a requierments files but making sure that pip is fully upgraded is always a good idea.
# The Future
So far we do not have a dependencies file and automatic installer, I am looking at adding a more robust GUI, or a double window app, honestly not to sure right now. If you do not have Tkinter installed that will be an automatic issue (but it's a built in lib so it should be fine, if not thats a bigger issue). 
# BUGS
If you CTRL + c the file it wont close untill you go back to the window(its weird, I dunno), besides this, no known bugs however i havent fully tested it so i honestly have no real idea...