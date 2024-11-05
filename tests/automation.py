# Import Mouse, Keyboard, and Keycodes
from zero_hid import Mouse, Keyboard, KeyCodes
from time import sleep
import subprocess
# Find out how to connect to HDMI-CSI

# Determine if OS is setup

# If not Setup
    # Find Blue Pixel
    
    # Press Button
# Check for Window's Updates
with Keyboard() as k, Mouse(absolute=False) as rel_mouse, Mouse(absolute=True) as abs_mouse:
    subprocess.call(['sh', './usb_gadget/video.sh'])
    OS = {
    "version": "Windows 10"
    }
    if OS["version"] == "Windows 11":
        abs_mouse.move(30500,7000)
    elif OS["version"] == "Windows 10":
        abs_mouse.move(8800,7100)
    k.press([KeyCodes.MOD_LEFT_GUI])
    sleep(3)
    k.type("windows updates")
    sleep(3)
    k.press([], KeyCodes.KEY_ENTER)
    k.press([], KeyCodes.KEY_ESC)
    sleep(5)
    rel_mouse.left_click()
