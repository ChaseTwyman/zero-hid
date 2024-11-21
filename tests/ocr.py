import cv2, pytesseract
from os import path
from take_screenshot import take_screenshot
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
    def __init__(self, text, cropped, *args):
        self.cropped = cropped
        self.text = text
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
        return pytesseract.image_to_data(self.image, output_type=Output.DICT)
    def __exit__(self, *args): {}