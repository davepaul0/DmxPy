## DmxPy - Python Controller for USB - DMX devices

DmxPy is a super-lightweight Python library for controlling any USB-DMX device that is compatible with Enttec's DMXUSB Pro.  This includes all Dmxking ultraDMX devices.

DmxPy requires PySerial to work - http://pyserial.sourceforge.net/

To import:
<code>from DmxPy import DmxPy</code>

To initialize:
<code>dmx = DmxPy('serial port')</code>
Where 'serial port' is where your device is located.


