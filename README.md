## DmxPy - Python Controller for USB - DMX devices

This is a Python 3 port of [DmxPy](https://github.com/davepaul0/DmxPy).

DmxPy is a super-lightweight Python library for controlling any USB-DMX device that is compatible with Enttec's DMXUSB Pro.  This includes all Dmxking ultraDMX devices.

DmxPy requires PySerial to work - http://pyserial.sourceforge.net/

To import:<br />
<code>from DmxPy import DmxPy</code>

To initialize:<br />
<code>dmx = DmxPy('serial port')</code>
Where 'serial port' is where your device is located.

To set a channel's value:<br />
<code>dmx.setChannel(chan, value)</code>
Where 'chan' and 'value' are integers representing the respective DMX channels and values to set!

To push dmx changes to device:<br />
<code>dmx.render()</code>
You need to call this to update the device!

