# i3autofloat

Hack that makes I3 "remeber" when an application is toggled to floating mode

## USE

- place this script on a folder in your PATH, 
- make it executable > chmod u+x [path/to/the/script]
- make sure all the paths are correct in the constants inside the script
- add the following keybind to ~/.config/i3/config
- bindsym $mod+Shift+space floating toggle; exec $HOME/bin/autofloat.py
- replace the location of your bin folder in the above line if needed


