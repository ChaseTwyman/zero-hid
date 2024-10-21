import random
from zero_hid import Keyboard, KeyCodes
number = 0
with Keyboard() as k:
    for i in range(1, 11):
        num1 = random.randint(1,100)
        num2 = random.randint(1,10000)
        num3 = random.randint(1,20)
        num5 = random.randint(1,2)
        number += num1
        number -= num2
        number *= num3
        number = number ** (1/num5) if number >= 0 else -number ** (1/num5)
        k.type(str(number))
        k.press([], KeyCodes.KEY_ENTER)