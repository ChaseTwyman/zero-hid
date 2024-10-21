import random
from zero_hid import Keyboard, KeyCodes
from time import sleep
number = 2
sleep(5)
with Keyboard() as k:
    for i in range(1, 1001):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        number *= num1
        number /= num2
        k.type(str(number))
        k.press([], KeyCodes.KEY_ENTER)