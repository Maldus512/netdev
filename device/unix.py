from evdev import UInput, ecodes as e
from evdev import AbsInfo
from utils import keydict
import time


class Device(object):

    def __init__(self):
        self.ui = UInput()


    def send(self, data):
        for d in data:
            self.ui.write(e.EV_KEY, keydict[d], 1)
            self.ui.syn()
            self.ui.write(e.EV_KEY, keydict[d], 0)
            self.ui.syn()


    def close(self):
        self.ui.close()


#cap = {
#        e.EV_KEY: [e.BTN_RIGHT, e.KEY_C],
#        e.EV_ABS: [(e.ABS_X, AbsInfo(value=128, min=0, max=255, fuzz=0, flat=15, resolution=0))]
#        }
#
#ui = UInput(cap, name="ciao")
#
#ui.write(e.EV_KEY, e.BTN_RIGHT, 1)
#ui.syn()
#time.sleep(0.1)
#ui.write(e.EV_KEY, e.BTN_RIGHT, 0)
#ui.syn()
#ui.close()
