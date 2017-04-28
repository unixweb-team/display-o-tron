#!/usr/bin/env python3

#needed commands
#pip3 install paho-mqtt
#curl https://get.pimoroni.com/displayotron | bash

import paho.mqtt.client as mqtt  
import dothat.backlight as backlight
import dothat.lcd as lcd  #import for display
import dothat.touch as nav  #import for buttons

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
            
    def replace_line(file_name, line_num, text):
        lines = open(file_name, 'r').readlines()
        lines[line_num] = text  #to save sensor values to call later
        out = open(file_name, 'w')
        out.writelines(lines)
        out.close()
    
    if msg.topic.find('/374586/') != -1:  #checks if the topic is the needed one
        if msg.topic.find('sensor1') != -1:
            #lcd.set_cursor_position(0,0)
            value = str(msg.payload).strip("b")  #strips unneeded parts from the values
            value = value.strip("'")
            replace_line('temp.txt', 0, value)
            #lcd.write('pm10 ' + value)
            
        if msg.topic.find('sensor2') != -1:
            #lcd.set_cursor_position(11,0)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            #lcd.write('pm25')
            #lcd.set_cursor_position(11, 1)  #writes the numerical value under the word
            colours(float(value))
            replace_line('temp.txt', 1, value)
            #lcd.write(value)
            
        if msg.topic.find('sensor3') != -1:
            #lcd.set_cursor_position(0,1)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            replace_line('temp.txt', 2, value)
            #lcd.write('temp ' + value)
            
        if msg.topic.find('sensor4') != -1:
            #lcd.set_cursor_position(0,2)
            value = str(msg.payload).strip("b")
            value = value.strip("'")
            replace_line('temp.txt', 3, value)
            #lcd.write('hum ' + value)     

@nav.on(nav.LEFT)
def handle_left(ch, evt):
    lcd.clear()
    lcd.set_cursor_position(0,0)
    tempfile = open('temp.txt', 'r').readlines()
    lcd.write("pm10:" + float(tempfile[0]))
    lcd.set_cursor_position(0, 1)
    lcd.write("pm25:"+ float(tempfile[1]))
    tempfile.close()

@nav.on(nav.RIGHT)
def handle_right(ch, evt):
    lcd.clear()
    lcd.set_cursor_position(0,0)
    tempfile = open('temp.txt', 'r').readlines()
    lcd.write("temp:" + float(tempfile[2]))
    lcd.set_cursor_position(0, 1)
    lcd.write("humidity:"+ float(tempfile[3]))
    tempfile.close()
    
backlight.off()  #clears colours
client = mqtt.Client()
client.connect("mqtt.unixweb.de",1883,60)  #connects to the broker

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

    
    
    
    
    
    
    
    
    
