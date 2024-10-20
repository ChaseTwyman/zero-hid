import random
from zero_hid import Keyboard
random_int = random.randint(0, 1114111)
character = chr(random_int)
with Keyboard() as k:
    k.type(character)
