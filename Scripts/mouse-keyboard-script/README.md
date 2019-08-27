# CPU_interation_logs

First we need to check the ids of the mouse and the keyboard using xinput --list
Take the id's and add them to the scripts in the np hup scrpits in place of the ids.
Also replace the user name by your computer's username and congrats it'll start woking.

nohup xinput test id > /home/username/Downloads/keyboard_log.txt 2>&1 &
