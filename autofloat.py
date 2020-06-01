#!/usr/bin/python3

## USE:
## place this script on a folder in your PATH, 
## make it executable > chmod u+x <path to the script> 
## make sure all the paths are correct in the constants bellow
## aad the following keybind to ~/.config/i3/config
## bindsym $mod+Shift+space floating toggle; exec $HOME/bin/autofloat.py
## replace the location of your bin folder in the above line

from subprocess import Popen, PIPE
from os import environ
import shutil

XPROP = '/usr/bin/xprop'
I3CONFIG = environ['HOME'] + '/' + '.config/i3/config'
I3CFGBCK = I3CONFIG + ".bck"
INDENTIFIER = "##autofloat##"
I3MSG = "/usr/bin/i3-msg"

def addfloat(wmclass):
    "Adds the float entry"
    line = 'for_window [class="%s"] floating enable ##autofloat## %s\n' % (wmclass, wmclass)
    open(I3CONFIG, 'a').write(line)

def removefloat(wmclass):
    """ removes the float entry"""
    for idx, line in enumerate(conf):
        if '##autofloat## %s\n' % (wmclass) in line:
            del conf[idx];
    open(I3CONFIG, 'w').writelines(conf)


def get_active_window_class():
    """Returns the windo class of the active window"""
    cmd = [XPROP, "-root", "32x", "'\t$0'", "_NET_ACTIVE_WINDOW"]
    output = Popen(cmd,stdout=PIPE).communicate()
    window_id = output[0].split()[1]
    cmd = [XPROP, "-id", window_id, "WM_CLASS"]
    output = Popen(cmd, stdout=PIPE).communicate()
    output = output[0].decode()
    output = output.split('=')[1].split(',')[1]
    output = output.strip().replace('"',"")
    return output

conf = open(I3CONFIG).readlines()
floating = [l.split()[-1] for l in conf if "##autofloat##" in l] 

#make a backup of the current config
shutil.copyfile(I3CONFIG, I3CFGBCK)

#add or remove active window 
wmclass = get_active_window_class()
if wmclass in floating:
    removefloat(wmclass)
else:
    addfloat(wmclass)

#reload i3
cmd = [I3MSG, "reload"]
pp = Popen(cmd)





