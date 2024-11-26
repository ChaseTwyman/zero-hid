import subprocess
from time import sleep
class Connect_Display:
    def __init__(self):
        if subprocess.run(['v4l2-ctl', '--set-dv-bt-timings', 'query'], capture_output=True, text=True).stdout.lower() == "bt timings set\n": return
        subprocess.call(['v4l2-ctl', '--set-edid=file=zero-hid/1080p30edid'])
        sleep(5)
        i = False
        while i == False:
            if subprocess.run(['v4l2-ctl', '--set-dv-bt-timings', 'query'], capture_output=True, text=True).stdout.lower() == "bt timings set\n":
                i = True
                return
            sleep(5)
    def __enter__(self): {}
    def __exit__(self, *args): {}