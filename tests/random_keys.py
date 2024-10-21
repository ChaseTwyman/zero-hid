import random
from zero_hid import Keyboard, KeyCodes
number = 0
with Keyboard() as k:
    for i in range(1, 1001):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        num3 = random.randint(1,20)
        num4 = random.randint(1,20)
        num5 = random.randint(1,2)
        num6 = random.randint(1,2)
        number += num1
        number -= num2
        number *= num3
        number /= num4
        number **= num5
        number **= 1/num6
        k.type(str(number))
        k.press([], KeyCodes.KEY_TAB)