# LinuxAlarm
A simple script based alarm clock

## Installation
* Install webbrowser module using `pip install webbrowser`.
* Clone the repository.
* Change the time of alarm in alarm.py according to your need.
* Setup up a cronjob.

### Setting up a cronjob
* Go to your terminal and run the following command : `crontab -e`
* Edit the file with [minutes] * * * * `cd /path_to_cloned_directory/ && ./alarmscript.sh` where [minutes] is same as the minutes you have set in your alarm.
* Save and exit.

### Alternatively you can also use `at` command
* Go to your terminal and run the following command : `echo "cd /path_to_cloned_directory/ && ./alarmscript.sh | at [time]"` where [time] is the time at which you want your alarm to go off.
