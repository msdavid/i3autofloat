# i3autofloat

Hack that makes I3 "remeber" when an application is toggled in or out of floating mode

## USE
Before anything make a copy of your i3 config file somewhere safe.  
This is quick hack that I made for myself. It has been minimally tested and possibly buggy.  
It might not be the most elegant, but works great for me
Ping me if you need help.  
 
- place this script on a folder in your PATH, 
- make it executable > chmod u+x [path/to/the/script]
- make sure all the paths are correct in the constants inside the script
- add the following keybind to ~/.config/i3/config
- bindsym $mod+Shift+space floating toggle; exec $HOME/bin/autofloat.py
- replace the location of your bin folder in the above line if needed

Use the togle float keybindig. the script will add a line in your i3 config file and reload i3. next time you open the same app, i3 will "remember" the last floating state.  

tested (only) on Debian 10 with i3 version 4.18 (2020-02-17)


