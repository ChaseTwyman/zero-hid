# Import Mouse, Keyboard, and Keycodes
from zero_hid import Mouse, Keyboard, KeyCodes
from connect_display import Connect_Display
from take_screenshot import take_screenshot
from move_mouse import Move_Mouse
from ocr import OCR, text_finder
from time import sleep
import subprocess
# Find out how to connect to HDMI-CSI

# Determine if OS is setup

# If not Setup
    # Find Blue Pixel
    
    # Press Button
# Check for Window's Updates
OS = {
    "version": ""
}
Checklist = {
    "Windows Update" : False,
    "Install Apps" : False,
    "Clean Temporary Files" : False,
    "Optimize Drive" : False,
    "Documentation" : {
        "Manufacturer" : "",
        "Model" : "",
        "Processor" : "",
        "Modem" : "",
        "Serial Number" : "",
        "Express Code" : "" #Base10 Representation of Base36 Serial Numebr
    }
}
with Keyboard() as k, Mouse(absolute=False) as rel_mouse, Mouse(absolute=True) as abs_mouse:
    with Connect_Display() as connect: {}
    z = False
    while z == False:
        with OCR(True, {"width":63, "height":23, "x":671, "y":1034}, "os_screenshot") as os_screenshot: {} # Checks for Windows 11 Search Bar
        if os_screenshot.lower() == "search\n":
            OS["version"] = "Windows 11"
            z=True
            break
        with OCR(True, {"width":170, "height":25, "x":107, "y":1043}, "os_screenshot") as os_screenshot: {} # Checks for Windows 10 Search Bar
        if os_screenshot.lower() == "type here to search\n":
            OS["version"] = "Windows 10"
            z =True
            break
        # If niether returns true, then assume computer is on login screen or not on desktop and try to login assuming no password
        k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_D) # Goes to Desktop if on a fullscreen window
        sleep(1)
        k.press([], KeyCodes.KEY_SPACE)
        sleep(3)
        k.press([], KeyCodes.KEY_SPACE)
    
    # Check for Windows Updates

    # Open Settings
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_I)
    sleep(1)
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_UP)

    if OS["version"] == "Windows 10":
        with OCR(True, {"width":148, "height":21, "x":878, "y":658}, "update_path") as update_path:
            if update_path.lower() == "update & security\n":
                with Move_Mouse(74+888, 10+668) as mouse_move: {}
                sleep(1)
                rel_mouse.left_click()
                with text_finder(True, {"width":1530-400, "height":1030, "x":400, "y":0}, "update_window") as found_text:
                    download_button = 0
                    for i in range(0,len(found_text[0])):
                        if "quality" == found_text[0][i].lower():
                            download_button = 1
                            break
                    for i in range(len(found_text[0]), 0):
                        if "download" == found_text[0][i].lower():
                            if download_button == 0:
                                with Move_Mouse(found_text[1][i][2], found_text[1][i][3]) as mouse_move: {}
                                break
                            else:
                                download_button -= 1
"""



    if OS["version"] == "Windows 11":
        with OCR(True, 238-80, 819-794, 80, 794, "update_path") as update_path:
            if update_path.lower() == "windows update"

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
"""