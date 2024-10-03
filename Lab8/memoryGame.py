import time
from machine import Pin
import random

buttonFlag = -1
debounceTime = 0

Random_LED = 0 #random LED turned on
Score = 0 # start the player with a score of 0

# Pin definititions
buttonPin = [28, 27, 26, 22]
ledPin = [10, 11, 12, 13]

# Pin setup
buttonPin0 = Pin(buttonPin[0], Pin.IN, Pin.PULL_UP)
buttonPin1 = Pin(buttonPin[1], Pin.IN, Pin.PULL_UP)
buttonPin2 = Pin(buttonPin[2], Pin.IN, Pin.PULL_UP)
buttonPin3 = Pin(buttonPin[3], Pin.IN, Pin.PULL_UP)

ledPin0 = Pin(ledPin[0], Pin.OUT)
ledPin1 = Pin(ledPin[1], Pin.OUT)
ledPin2 = Pin(ledPin[2], Pin.OUT)
ledPin3 = Pin(ledPin[3], Pin.OUT)

# Interrupt Definitions
def button0Pressed(buttonPin0):
    print("button 0")
    global buttonFlag, debounceTime
    if(time.ticks_ms() - debounceTime) > 500:
        buttonFlag = 0
        debounce_time=time.ticks_ms()

def button1Pressed(buttonPin1):
    print("button 1")
    global buttonFlag, debounceTime
    if(time.ticks_ms() - debounceTime) > 500:
        buttonFlag = 1
        debounce_time=time.ticks_ms()

def button2Pressed(buttonPin2):
    print("button 2")
    global buttonFlag, debounceTime
    if(time.ticks_ms() - debounceTime) > 500:
        buttonFlag = 2
        debounce_time=time.ticks_ms()

def button3Pressed(buttonPin3):
    print("button 3")
    global buttonFlag, debounceTime
    if(time.ticks_ms() - debounceTime) > 500:
        buttonFlag = 3
        debounce_time=time.ticks_ms()

# Interrupt setup
buttonPin0.irq(trigger=Pin.IRQ_FALLING, handler = button0Pressed)
buttonPin1.irq(trigger=Pin.IRQ_FALLING, handler = button1Pressed)
buttonPin2.irq(trigger=Pin.IRQ_FALLING, handler = button2Pressed)
buttonPin3.irq(trigger=Pin.IRQ_FALLING, handler = button3Pressed)

#make sure all the LEDs are off
ledPin0.off()
ledPin1.off()
ledPin2.off()
ledPin3.off()

while True:
    Random_LED = random.randint(0,3)
    if(Random_LED == 0):
        print("LED 0")
        ledPin0.on()
    if(Random_LED == 1):
        print("LED 1")
        ledPin1.on()
    if(Random_LED == 2):
        print("LED 2")
        ledPin2.on()
    if(Random_LED == 3):
        print("LED 3")
        ledPin3.on()

    # time.sleep(200) #delay for 2 second

    # turn off all LEDs
    ledPin0.off()
    ledPin1.off()
    ledPin2.off()
    ledPin3.off()

    #check if the correct button was pressed
    if buttonFlag is Random_LED:
        buttonFlag = -1 #clear the interrupt
        Score = Score + 1
        print("Score: ", Score)