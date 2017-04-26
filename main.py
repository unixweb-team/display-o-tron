#!/usr/bin/env python3

#needed commands
#pip3 install paho-mqtt
#curl https://get.pimoroni.com/displayotron | bash

import paho.mqtt.client as mqtt  
import dothat.lcd as lcd  #import for display

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " +str(rc))
    client.subscribe('#')

def on_message(client, userdata, msg):  #triggers on an update
    if msg.topic.find('/374586/') != -1:  #checks if the topic is the needed one
        if msg.topic.find('sensor1') != -1:
            lcd.set_cursor_position(0,0)
            value = str(msg.payload).strip("b")  #strips unneeded parts from the values
            value = value.strip("'")
            lcd.write('pm10 ' + value)
            
        if msg.topic.find('sensor2') != -1:
            lcd.set_cursor_position(11,0)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            lcd.write('pm25')
            lcd.set_cursor_position(11, 1)  #writes the numerical value under the word
            lcd.write(value)
            
        if msg.topic.find('sensor3') != -1:
            lcd.set_cursor_position(0,1)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            lcd.write('temp ' + value)
            
        if msg.topic.find('sensor4') != -1:
            lcd.set_cursor_position(0,2)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            lcd.write('hum ' + value)
    
client = mqtt.Client()
client.connect("mqtt.unixweb.de",1883,60)  #connects to the broker

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
