USER_HOME=$(getent passwd $SUDO_USER | cut -d: -f6 | tail -n 1)
v4l2-ctl --set-edid=file="$USER_HOME/TC358743-Driver/1080p25edid"
test