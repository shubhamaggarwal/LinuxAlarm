#!/usr/bin/env python

import webbrowser
import datetime

current_time = datetime.datetime.now()

current_hours = int(current_time.strftime("%H"))
current_minutes = int(current_time.strftime("%M"))

# Setup the time of alarm here.
hours = 9
minutes = 30

if (current_hours >= hours and current_minutes >= minutes) or current_hours >= hours + 1: 
    webbrowser.open("/media/canoodle/Data/MUSIC/9.mp3")
