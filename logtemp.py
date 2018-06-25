#!/usr/bin/python

import Adafruit_DHT
import time
import datetime

horario = datetime.datetime.now()

sensor = Adafruit_DHT.DHT22
pin = 14

file = open("temperature.txt","a")

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
#    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    file.write(datetime.datetime.now().strftime("%d-%m-%y-%H:%M"))
    file.write(';')
    file.write('{0:0.1f};{1:0.1f}\n'.format(temperature, humidity))
    file.close()
else:
    print('Failed to get reading. Try again!')

