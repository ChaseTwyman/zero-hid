# Import Mouse, Keyboard, and Keycodes
from zero_hid import Mouse, Keyboard, KeyCodes
from connect_display import Connect_Display
from take_screenshot import take_screenshot
from time import sleep, perf_counter
from Move_Mouse import move_mouse
from ocr import OCR, text_finder
import subprocess
# Find out how to connect to HDMI-CSI

# Determine if OS is setup

# If not Setup
    # Find Blue Pixel
    
    # Press Button
# Check for Window's Updates
constants = {
    "repeat_num" : 5,
    "original_scaling": ""
}
OS = {
    "version": "",
    "Rely on OCR": False
}
Checklist = {
    "Windows Update" : {
        "Check for Updates" : False,
        "Install Updates" : False
    },
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

# Functions
def retry(function, threshold):
    for i in range(threshold):
        if function == True or function != -1:
            return True
    return False
def duplicate_display():
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_R)
    sleep(3) # Probably needs a conditional
    k.type("DisplaySwitch.exe /clone")
    k.press([], KeyCodes.KEY_ENTER)
    sleep(5)
    Connect_Display()
def determine_OS(not_first_time = False): # Checks for and Saves OS Version
    if (OCR(True, {"width":63, "height":23, "x":671, "y":1034}, "os_screenshot")).__enter__().lower() == "search\n": # Checks for Windows 11 Search Bar
        OS["version"] = "Windows 11"
        return True
    if OCR(True, {"width":170, "height":25, "x":107, "y":1043}, "os_screenshot").__enter__().lower() == "type here to search\n": # Checks for Windows 10 Search Bar
        OS["version"] = "Windows 10"
        return True
    if text_finder(True, {"width":390-83, "height":1073-1027, "x":83, "y":1027}, "scaled_os_screenshot").containsNCS("Type") > -1:
        OS["version"] = "Windows 10"
        return True
    if text_finder(True, {"width":960, "height":180, "x":0, "y":900}, "larger_scaled_os_screenshot").containsNCS("Search") > -1:
        OS["version"] = "Windows 11"
        return True
    if text_finder(True, {"width":960, "height":180, "x":0, "y":1000}, "larger_scaled_os_screenshot").containsNCS("Search") > -1:
        OS["version"] = "Windows 11"
        return True
    else:
        print(OCR(False, "larger_scaled_os_screenshot").__enter__())
    # If niether returns true, then assume computer is on login screen or not on desktop and try to login assuming no password
    if not_first_time:
        k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_D) # Goes to Desktop if on a fullscreen window
        sleep(1)
        k.press([], KeyCodes.KEY_SPACE)
        sleep(3)
        k.press([], KeyCodes.KEY_SPACE)
    else:
        k.press([], KeyCodes.KEY_SPACE)
        sleep(3)
        with open('passwords.txt', 'r') as file:
            k.type(file.readline())
        k.press([], KeyCodes.KEY_ENTER)
    return False
def set_scaling():
    # Open Settings
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_I)
    if OS["version"] == "Windows 10":
        sleep(1) # Might Need a conditional
        k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_UP)
        for i in range(10):
            if text_finder(True, {"width":175, "height":43, "x":0, "y":0}, "settings_corner_screenshot").containsNCS("Settings") > -1:
                break
            if i >= 9:
                return False
        system_settings_text = text_finder(True, {"width":405-141, "height":583-315, "x":141, "y":315}, "System_screenshot")
        if system_settings_text.containsNCS("System") > -1:
            system_settings_text.goto_text(141, 315)
            for i in range(5):
                if text_finder(True, {"width":757-340, "height":165-57, "x":340, "y":57}, "display_corner_screenshot").containsNCS("Display") > -1:
                    break
                if i >= 4:
                    print("There was an error trying to set scaling (finding the display screen)")
                    return False
            for i in range(9):
                k.press([], KeyCodes.KEY_TAB)
                if i < 8: sleep(0.1)
            scaling_button = text_finder(True, {"width":681-351, "height":1013-932, "x":351, "y":932}, "scale_button_screenshot")
            scales = ["100%", "150%", "175%"]
            if scaling_button.containsNCS("125%") == -1:
                for i in scales:
                    if scaling_button.containsNCS(i) > -1:
                        scaling_button.goto_text(351, 932)
                        scaling_button_options = text_finder(True, {"width":686-350, "height":1005-758, "x":350, "y":758}, "scale_button_options_screenshot")
                        if scaling_button_options.containsNCS("125%") > -1:
                            location = scaling_button_options.goto_text(350, 758)
                            sleep(5)
                            k.press([KeyCodes.MOD_LEFT_ALT], KeyCodes.KEY_LEFT)
                            constants["original_scaling"] = i
                            return True
                    if i == scales[-1]:
                        print("Unsupported Display Size or Resolution")
                        return False
            else:
                constants["original_scaling"] = "125%"
                k.press([KeyCodes.MOD_LEFT_ALT], KeyCodes.KEY_LEFT)
                return True
        else:
            print("Could not find system settings button")
            return False
    elif OS["version"] == "Windows 11":
        k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_DOWN)
        sleep(0.5)
        k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_DOWN)
        sleep(0.5)
        k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_UP)
        sleep(0.5)
        k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_UP)
def check_for_updates():
    # Open Settings

    if OS["version"] == "Windows 10":
        sleep(3)
        if OCR(True, {"width":148, "height":21, "x":878, "y":658}, "update_path").__enter__().lower() == "update & security\n":
            move_mouse(74+888, 10+668)
            sleep(1)
            rel_mouse.left_click()
        else:
            whole_screen = text_finder(False, "update_path", new_image = True)
            if whole_screen.containsNCS("Security") > -1:
                whole_screen.goto_text()
            else:
                print("There was an error finding the Windows Update Settings Icon")
                return False
        for i in range(10):
            if OCR(True, {"width":691-425, "height":115-68, "x":425, "y":68}, "windows_update_title").__enter__().lower() == "windows update\n":
                break
            if i >= 4:
                print("There was an error clicking the Windows Update Settings Icon")
                return False
        found_text = text_finder(True, {"width":1530-400, "height":1030, "x":400, "y":0}, "update_window")
        if found_text.containsNCS("Install") > -1: found_text.goto_text(400, 0)
        if OCR(True, {"width":1137-1059, "height":591-567, "x":1059, "y":567}, "get_latest_updates_prompt").__enter__().lower() == "not now\n":
            move_mouse(1059+(1137-1059)/2, 567+(591-567)/2)
            sleep(0.1)
            rel_mouse.left_click()
        found_text = text_finder(True, {"width":1530-400, "height":1030, "x":400, "y":0}, "update_window")
        if found_text.containsNCS("Download") > -1: found_text.goto_text(400, 0)
        if OCR(True, {"width":592-445, "height":250-230, "x":445, "y":230}, "check_for_update_button").__enter__().lower() == "check for updates\n":
            move_mouse(445+(592-445)/2, 230+(250-230)/2)
            sleep(0.1)
            rel_mouse.left_click()
            Checklist["Windows Update"]["Check for Update"] = True
            return True
        elif found_text.containsNCS("Download") > -1:
            found_text.goto_text(400, 0)
            Checklist["Windows Update"]["Check for Update"] = True
            return True
        elif found_text.containsNCS("Downloading") > -1 or found_text.containsNCS("Installing") > -1 or found_text.containsNCS("Required") > -1:
            Checklist["Windows Update"]["Check for Update"] = True
            return True
        else:
            print("Could not find Check for Updates Button")
            return False

    if OS["version"] == "Windows 11":
        if not OS["Rely on OCR"]:
            with OCR(True, {"width":238-80, "height":819-794, "x":80, "y":794}, "update_path") as update_path:
                complete = False
                for i in range(0, constants["repeat_num"]):
                    if update_path.lower() == "windows update\n":
                        with move_mouse(80+(238-80)/2, 794+(819-794)/2) as mouse_move: {}
                        sleep(1)
                        rel_mouse.left_click()
                        complete = False
                        for i in range(0, constants["repeat_num"]):
                            with OCR(True, {"width":1862-1697, "height":249-224, "x":1697, "y":224}, "check_for_update_button") as button:
                                if button.lower() == "check for updates\n":
                                    with move_mouse(1697+(1862-1697)/2, 224+(249-224)/2) as mouse_move: {}
                                    sleep(1)
                                    rel_mouse.left_click()
                                    complete = True
                                    Checklist["Windows Update"]["Check for Updates"] = True
                                    break
                            if i == constants["repeat_num"] and not complete:
                                print("error clicking windows button")
                        complete = True
                        break
                    else:
                        complete = False
                    if i == constants["repeat_num"] and not complete:
                        print("error occured when checking for windows update path")
def install_software():
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_R)
    sleep(3)
    k.type('"D:\\New Windows Setup.exe"')
    k.press([], KeyCodes.KEY_ENTER)
    sleep(10)
    k.press([], KeyCodes.KEY_LEFT)
    sleep(0.1)
    k.press([], KeyCodes.KEY_ENTER)
    sleep(3)
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_R)
    sleep(3)
    k.type('D:\\Reader_en_install.exe')
    k.press([], KeyCodes.KEY_ENTER)
    sleep(10)
    k.press([], KeyCodes.KEY_LEFT)
    sleep(0.1)
    k.press([], KeyCodes.KEY_ENTER)
def clear_temp():
    k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_R)
    sleep(3)
    k.type('cleanmgr.exe')
    k.press([], KeyCodes.KEY_ENTER)
    sleep(5)
    k.press([KeyCodes.MOD_LEFT_ALT, KeyCodes.MOD_LEFT_SHIFT], KeyCodes.KEY_TAB)
    sleep(3)
    k.press([], KeyCodes.KEY_DOWN)
    k.press([], KeyCodes.KEY_SPACE)
    k.press([], KeyCodes.KEY_END)
    k.press([], KeyCodes.KEY_SPACE)
    k.press([], KeyCodes.KEY_UP)
    k.press([], KeyCodes.KEY_UP)
    k.press([], KeyCodes.KEY_SPACE)
    k.press([], KeyCodes.KEY_TAB)
    k.press([], KeyCodes.KEY_TAB)
    k.press([], KeyCodes.KEY_TAB)
    k.press([], KeyCodes.KEY_SPACE)
    k.press([], KeyCodes.KEY_SPACE)
with Keyboard() as k, Mouse() as rel_mouse:
    timer1 = perf_counter()
    rel_mouse.move(1,0)
    rel_mouse.move(-1,0)

    # Command 1
    Connect_Display()
    
    timer2 = perf_counter()
    print(f"Time to Connect Display: {timer2 - timer1:.6f} seconds\n")
    # Check if Computer is in Duplicate Display Mode
    
    # Command 2
    if not determine_OS() and not determine_OS(True) and not retry(determine_OS(True), 15): print("An Error Occurred when trying to determine OS Version")

    timer3 = perf_counter()
    print(f"Time to Determine OS: {timer3 - timer2:.6f} seconds\n")

    # Command 3
    duplicate_display()

    timer4 = perf_counter()
    print(f"Time to Duplicate Display: {timer4 - timer3:.6f} seconds\n")
    
    # Command 4
    if not set_scaling():
        print("An Error Occurred when trying to set scaling to 125%")
        OS["Rely on OCR"] = True
    
    timer5 = perf_counter()
    print(f"Time to Set Scaling: {timer5 - timer4:.6f} seconds\n")

    # Task 1
    if not check_for_updates(): print("An Error Occurred when Checking for Windows Updates") # Check for Windows Updates
    else:
        if Checklist["Windows Update"]["Check for Update"] != True:
            Checklist["Windows Update"]["Check for Update"] = True
        k.press([KeyCodes.MOD_LEFT_ALT], KeyCodes.KEY_F4)

    timer6 = perf_counter()
    print(f"Time to Check for Windows Updates: {timer6 - timer5:.6f} seconds\n")

    # Task 2
    install_software()
    # Check later if software installed correctly

    timer7 = perf_counter()
    print(f"Time to Install Software: {timer7 - timer6:.6f} seconds\n")

    # Task 3
    clear_temp()
    # Clears Temporary Files
    
    timer8 = perf_counter()
    print(f"Time to Install Software: {timer8 - timer7:.6f} seconds\n")

    print(f"Total Time: {timer8 - timer1:.6f} seconds\n")