import cv2, os
from ocr import OCR
class crop_image:
    def __init__(self, path):
        self.path = path if path[-4:] == ".png" else path + ".png"
    def __enter__(self): {}
    def __exit__(self, *args):
        cv2.write(self.path,cv2.imread(self.path))
with crop_image("win10") as win10:
    with OCR("win10") as text:
        print(text)