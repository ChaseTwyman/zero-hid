from zero_hid import Mouse, Keyboard, KeyCodes
from time import sleep
with Keyboard() as k, Mouse() as rel_mouse:
    sleep(2)
    k.press([KeyCodes.MOD_LEFT_ALT], 0, False)
    sleep(1)
    k.press([KeyCodes.MOD_LEFT_SHIFT], KeyCodes.KEY_TAB)
    sleep(0.5)
    # k.press([KeyCodes.MOD_LEFT_ALT, KeyCodes.MOD_LEFT_SHIFT], KeyCodes.KEY_TAB)