# Import Mouse, Keyboard, and Keycodes
from zero_hid import Mouse, Keyboard, KeyCodes
from time import sleep 
# Find out how to connect to HDMI-CSI

# Determine if OS is setup

# If not Setup
    # Find Blue Pixel
    
    # Press Button
# Check for Window's Updates
with Keyboard() as k, Mouse() as m:
    k.press([KeyCodes.MOD_LEFT_GUI])
    sleep(3)
    k.type("windows updates")
    sleep(3)
    k.press([], KeyCodes.KEY_ENTER)
    k.press([], KeyCodes.KEY_ESC)
    sleep(3)
    for i in range(1,4):
        k.press([], KeyCodes.KEY_TAB)
    k.press([], KeyCodes.KEY_ENTER)
