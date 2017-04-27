#!/usr/bin/env python3

#needed commands
#pip3 install paho-mqtt
#curl https://get.pimoroni.com/displayotron | bash

import paho.mqtt.client as mqtt  
import dothat.backlight as backlight
import dothat.lcd as lcd  #import for display

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " +str(rc))
    client.subscribe('#')

def on_message(client, userdata, msg):  #triggers on an update
    def colours(value):  #changes whole backlight based on numeric values
        if value > 40:
            backlight.rgb(238, 0, 0)  #red
        elif value > 30:
            backlight.rgb(238, 154, 0)  #orange
        elif value > 20:
            backlight.rgb(238, 238, 0)  #yellow
        elif value > 10:
            backlight.rgb(0, 238, 118)  #green
            
    if msg.topic.find('/374586/') != -1:  #checks if the topic is the needed one
        if msg.topic.find('sensor1') != -1:
            lcd.set_cursor_position(0,0)
            value = str(msg.payload).strip("b")  #strips unneeded parts from the values
            value = value.strip("'")
            lcd.write('pm10 ' + value)
            
            #temp = open('temp.txt', 'w')
            #temp.write(value)
            #temp.close()
            
        if msg.topic.find('sensor2') != -1:
            lcd.set_cursor_position(11,0)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            lcd.write('pm25')
            lcd.set_cursor_position(11, 1)  #writes the numerical value under the word
            colours(value)
            lcd.write(value)
            
            #tempfile = open('temp.txt', 'r')
            #temp = tempfile.readlines()[0]
            #value = float(value) + float(temp)
            #value = value / 2  #gets average value for colour of backlight
            #tempfile.close()

            #temp = open('temp.txt', 'w')
            #temp.write(str(value))  #writes value to file for usage later
            #temp.close()
            
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
            #tempfile = open('temp.txt', 'r')
            #temp = tempfile.readlines()[0]
            #colours(float(temp))
            #tempfile.close()            
    
backlight.off()  #clears colours
client = mqtt.Client()
client.connect("mqtt.unixweb.de",1883,60)  #connects to the broker

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

    
    
    
    
    
    
    
    
    
