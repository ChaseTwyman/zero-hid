from zero_hid import Mouse
import random
with Mouse() as m:
    for i in range(1000):
        y = random.randint(0,50)
        x = random.randint(0,50)
        posy = random.choice([-1,1])
        posx = random.choice([-1,1])
        m.move(x*posx,y*posy)
