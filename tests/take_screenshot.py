import subprocess
from os import path, remove
class take_screenshot:
    def __init__(self, file_name, cropped, *args):
        self.file_name = file_name if file_name[-4:] == ".png" else file_name + ".png"
        self.cropped = cropped
        if cropped:
            self.width = str(args[0])
            self.height = str(args[1])
            self.x = str(args[2])
            self.y = str(args[3])
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if path.exists(self.file_name): remove(self.file_name)
        if self.cropped:
            subprocess.call(
                ['ffmpeg', '-f', 'v4l2', '-i', '/dev/video0', '-vf',
                'select=eq(n\,1), crop=' + self.width + ':' + self.height + ':' + self.x + ':' + self.y,
                '-frames', '1', self.file_name])
        else:
            subprocess.call(['ffmpeg', '-f', 'v4l2', '-i', '/dev/video0', '-vf', 'select=eq(n\,1)', '-frames', '1', self.file_name])
            