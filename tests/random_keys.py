import random
from zero_hid import Keyboard, KeyCodes
with Keyboard() as k:
    for i in range(1, 1001):
        k.type(str(i))
        k.press([], KeyCodes.KEY_ENTER)