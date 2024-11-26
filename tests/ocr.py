import cv2, pytesseract
from take_screenshot import take_screenshot
from Move_Mouse import move_mouse
from pytesseract import Output
from zero_hid import Mouse
from time import sleep
from os import path, remove
class OCR:
    def __init__(self, cropped, *args):
        self.cropped = cropped
        if cropped:
            self.width = str(args[0]["width"])
            self.height = str(args[0]["height"])
            self.x = str(args[0]["x"])
            self.y = str(args[0]["y"])
            self.file_name = args[1] if args[1][-4:] == ".png" else args[1] + ".png"
            with take_screenshot(self.file_name, True, self.width, self.height, self.x, self.y) as screenshot: {}
        else:
            self.file_name = args[0] if args[0][-4:] == ".png" else args[0] + ".png"
            if not path.exists(self.file_name):
                with take_screenshot(self.file_name, False) as screenshot: {}
        self.image = cv2.imread(self.file_name)
    def __enter__(self):
        return pytesseract.image_to_string(self.image)
    def __exit__(self, *args): {}

class text_finder:
    def __init__(self, cropped, *args, new_image=False):
        self.cropped = cropped
        if cropped:
            self.width = str(args[0]["width"])
            self.height = str(args[0]["height"])
            self.x = str(args[0]["x"])
            self.y = str(args[0]["y"])
            self.file_name = args[1] if args[1][-4:] == ".png" else args[1] + ".png"
            with take_screenshot(self.file_name, True, self.width, self.height, self.x, self.y) as screenshot: {}
        else:
            self.file_name = args[0] if args[0][-4:] == ".png" else args[0] + ".png"
            if not path.exists(self.file_name):
                with take_screenshot(self.file_name, False) as screenshot: {}
            elif new_image:
                remove(self.file_name)
                with take_screenshot(self.file_name, False) as screenshot: {}

        self.image = cv2.imread(self.file_name)
        self.results = pytesseract.image_to_data(self.image, output_type=Output.DICT)
        self.position = -1
    
    def __enter__(self):
        coords = []
        for i in range(0, len(self.results["text"])):
            coords.append([self.results["width"][i], self.results["height"][i], self.results["left"][i], self.results["top"][i]])
        return [self.results["text"], coords]
    
    def containsNCS(self, text):
        try:
            self.position = [results.lower() for results in self.results["text"]].index(text.lower())
        except ValueError as _:
            self.position = -1
        return self.position

    def goto_text(self, x = 0, y = 0, click = True):
        self.offset_x = x
        self.offset_y = y
        coords = []
        for i in range(0, len(self.results["text"])):
            coords.append([self.results["width"][i], self.results["height"][i], self.results["left"][i], self.results["top"][i]])
        move_mouse(self.offset_x+coords[self.position][2]+int(coords[self.position][0]/2),
                   self.offset_y+coords[self.position][3]+int(coords[self.position][1]/2))
        if click:
            sleep(0.1)
            with Mouse() as rel_mouse:
                rel_mouse.left_click()

    def __exit__(self, *args): {}