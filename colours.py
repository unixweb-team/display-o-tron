import dothat.backlight as backlight
import time
for i in range(100):
    backlight.rgb(238, 0, 0)  #red
    time.sleep(5)
    backlight.rgb(238, 154, 0)  #orange
    time.sleep(5)
    backlight.rgb(238, 238, 0)  #yellow
    time.sleep(5)
    backlight.rgb(0, 238, 118)  #green
    time.sleep(5)
