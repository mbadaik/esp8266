
print('Main application starts..')
from machine import Pin
from umqtt.simple import MQTTClient
import dht
import machine
import time

mqtt_client = MQTTClient(client_id='ESP8266_TEMP_SENS', 
                    server='192.168.0.239')  
                    
                    
mqtt_client.connect()                   
mqtt_client.publish('hi','Hello from esp8266')

d = dht.DHT11(machine.Pin(2)) # DHT sensor connected to GPIO 2 is D4 in esp8266 
time.sleep(2)
while True:
  d.measure()
  mqtt_client.publish('temp',str(d.temperature()),retain=True)
  mqtt_client.publish('humid',str(d.humidity()),retain=True)
  print(d.temperature())
  print(d.humidity())
  time.sleep(30)
