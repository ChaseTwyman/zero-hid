from zero_hid import Mouse
class move_mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.border = {
            "x" : 11,
            "y" : 22
        }
        self.constant = {
            "x" : 17.063,
            "y" : 30.328
        }
        with Mouse(absolute=True) as m:
            m.move(self.border["x"]+int(self.constant["x"]*self.x),self.border["y"]+int(self.constant["y"]*self.y))
    def __enter__(self): {}
    def __exit__(self, *args): {}