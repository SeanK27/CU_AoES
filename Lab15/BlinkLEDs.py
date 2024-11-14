import time
from machine import Pin
import random



#creat level definition
global level
level = 0 #start the program at level 0

global speed 
speed = 2 #start the program at 2second 

ledPin = [13, 14, 15]

ledPin0 = Pin(ledPin[0], Pin.OUT)
ledPin1 = Pin(ledPin[1], Pin.OUT)
ledPin2 = Pin(ledPin[2], Pin.OUT)


while True:

    ledPin0.on()
    ledPin1.on()
    ledPin2.on()

    time.sleep(1)

    ledPin0.off()
    ledPin1.off()
    ledPin2.off()

    time.sleep(1)

    

