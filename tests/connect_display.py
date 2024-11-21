import subprocess
from os import path, remove
from time import sleep
from take_screenshot import take_screenshot
subprocess.call(['v4l2-ctl', '--set-edid=file=zero-hid/1080p30edid'])
sleep(10)
subprocess.call(['v4l2-ctl', '--set-dv-bt-timings', 'query'])
# with take_screenshot("os_screenshot", True, 63, 23, 671, 1034) as os_screenshot: {}
# with take_screenshot("os_screenshot", True, 660, 48, 45, 1022) as os_screenshot: {}