# Keyboard layout:
setxkbmap hu 

# Fuj fönti Esc
setxkbmap -option caps:escape

# Java Stuff:
export _JAVA_AWT_WM_NONREPARENTING=1 &

# DWM status
/home/lorant/.suckless/dwm-bar/dwm_bar.sh &
#/home/lorant/.suckless/slstatus/slstatus &

# Wallpaper
# nitrogen --restore &

# Pywal things:
wal -R &

# Alpha:
picom &

# Window transparency
xcompmgr &

# Window manager
exec dwm
