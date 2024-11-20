import cv2, os
class crop_image:
    def __init__(self, path_name, path):
        self.path_name = path_name
        self.path = path
    def crop_image (self):
        cv2.write(self.path_name,cv2.imread(self.path))