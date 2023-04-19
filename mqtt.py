import json
import paho.mqtt.client as mqttClient
import timefrom datetime
import datetimefrom pymodbus.constants 
import Endianfrom pymodbus.constants
import Defaultsfrom pymodbus.payload 
import BinaryPayloadDecoderfrom pymodbus.client.sync
import ModbusSerialClient as ModbusClientfrom pymodbus.transaction 
import ModbusRtuFramerfrom pymodbus.payload import BinaryPayloadBuilder
# settings for USB-RS485 adapterSERIAL = '/dev/ttyUSB0'BAUD = 9600# 
set Modbus defaultsDefaults.UnitId = 1
Defaults.Retries = 5
counter = 1
client = ModbusClient(method='rtu', port=SERIAL, stopbits=1, bytesize=8, timeout=3,baudrate=BAUD, parity='N')
connection = client.connect()
print(bool(connection))
def on_connect(client, userdata, flags, rc): 
  print(rc)    
  if rc == 0:    
    print(rc)  
    clientmqtt.subscribe("/Meter_Data") 
    global Connected            
    Connected = True       
   else: 
    print("Connection failed")
    Connected = False
