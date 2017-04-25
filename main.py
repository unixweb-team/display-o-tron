#!/usr/bin/env python3

import paho.mqtt.client as mqtt  
import dothat.lcd as lcd  #import for display

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " +str(rc))
    client.subscribe('#')

def on_message(client, userdata, msg):  #triggers on an update
    #need to add a clear display
    if msg.topic.find('/374586/') != -1:  #checks if the topic is the needed one
        #print(msg.topic + " " + float(msg.payload))
        if msg.topic.find('sensor1') != -1:
            lcd.set_cursor_position(0,0)
            lcd.write('pm10 ' + float(msg.payload))
            
        if msg.topic.find('sensor1') != -1:
            lcd.set_cursor_position(11,0)
            lcd.write('pm25 ' + float(msg.payload))
            
        if msg.topic.find('sensor1') != -1:
            lcd.set_cursor_position(0,1)
            lcd.write('temp ' + float(msg.payload))
            
        if msg.topic.find('sensor1') != -1:
            lcd.set_cursor_position(0,2)
            lcd.write('hum ' + float(msg.payload))
    
client = mqtt.Client()
client.connect("mqtt.unixweb.de",1883,60)  #connects to the broker

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
