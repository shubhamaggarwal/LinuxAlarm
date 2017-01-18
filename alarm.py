#!/usr/bin/env python

import webbrowser
import datetime

current_time = datetime.datetime.now()

hours = int(current_time.strftime("%H"))
minutes = int(current_time.strftime("%M"))

if (hours >= 9 and minutes >= 30) or hours >= 10: 
    webbrowser.open("/media/canoodle/Data/MUSIC/9.mp3")
