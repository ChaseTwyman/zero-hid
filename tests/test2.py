from zero_hid import Mouse
from time import sleep
with Mouse() as m:
    m.move(10,10)
    sleep(5)
    m.left_click()