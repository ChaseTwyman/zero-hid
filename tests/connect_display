import subprocess
from os import path, remove
from time import sleep
subprocess.call(['v4l2-ctl', '--set-edid=file=zero-hid/1080p30edid'])
sleep(10)
if path.exists("still_image.png"): remove("still_image.png")
subprocess.call(['v4l2-ctl', '--set-dv-bt-timings', 'query'])
subprocess.call(['ffmpeg', '-f', 'v4l2', '-i', '/dev/video0', '-vf', 'select=eq(n\,1)', '-frames', '1', 'still_image.png'])