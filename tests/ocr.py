import cv2
import pytesseract
class OCR:
    def __init__(self, file_name):
        self.file_name = file_name if file_name[-4:] == ".png" else file_name + ".png"
        self.image = cv2.imread(self.file_name)
    def __enter__(self):
        return pytesseract.image_to_string(self.image)
    def __exit__(self, *args): {}