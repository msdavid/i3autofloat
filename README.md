# i3autofloat

Hack that makes I3 "remeber" when an application is toggled in or out of floating mode

## USE
Before anything make a copy of your i3 config file somewhere safe.  
this is quick hack that I made for myself.   
It has been minimally tested, so might be broken.  
It might not be the most elegant, but works great in my system.  
Ping me if you need help.  
 
- place this script on a folder in your PATH, 
- make it executable > chmod u+x [path/to/the/script]
- make sure all the paths are correct in the constants inside the script
- add the following keybind to ~/.config/i3/config
- bindsym $mod+Shift+space floating toggle; exec $HOME/bin/autofloat.py
- replace the location of your bin folder in the above line if needed


