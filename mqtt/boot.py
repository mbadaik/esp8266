# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import os
import network
print('Hello world')

### connect to wifi ###
ssid = "WIFI-Nwetwork-Name"
password = "Password"
station = network.WLAN(network.STA_IF)
 
if station.isconnected() == False:
  station.active(True)
  station.connect(ssid, password)

print('Connected!', station.ifconfig())
###

gc.collect()
exec(open('./main.py').read(),globals())


