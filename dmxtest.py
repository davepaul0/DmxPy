from DmxPy import DmxPy
import time

dmx = DmxPy('/dev/ttyUSB0')
dmx.setChannel(1, 100)
dmx.setChannel(2, 50)
dmx.render()
time.sleep(2)
dmx.setChannel(3, 100)
time.sleep(2)
dmx.blackout()
dmx.render()