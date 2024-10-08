import time
from machine import Pin
import random


#creat level definition
global level
level = 0 #start the program at level 0

global speed 
speed = 2 #start the program at 2second 

#creat button flags
global buttonFlag0
global buttonFlag1
global buttonFlag2 
global buttonFlag3

buttonFlag0 = 0
buttonFlag1 = 0
buttonFlag2 = 0
buttonFlag3 = 0


#global debounceTime 
debounceTime = 0

global Random_LED 
Random_LED = 0  #random LED turned on

global Score # start the player with a score of 0
Score = 0 

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
def button0Pressed(buttonPin0,_):
#def button0Pressed(buttonPin0,_):
    print("button 0")
    global debounceTime, buttonFlag0
    if(time.ticks_ms() - debounceTime) > 500:
        buttonFlag0 = 1
        debounceTime=time.ticks_ms()

def button1Pressed(buttonPin1,_):
    print("button 1")
    global debounceTime, buttonFlag1
    if(time.ticks_ms() - debounceTime) > 500:
        buttonFlag1 = 1
        debounceTime=time.ticks_ms()

def button2Pressed(buttonPin2,_):
    print("button 2")
    global debounceTime, buttonFlag2
    if(time.ticks_ms() - debounceTime) > 500:
        buttonFlag2 = 1
        debounceTime=time.ticks_ms()

def button3Pressed(buttonPin3,_):
    print("button 3")
    global debounceTime, buttonFlag3
    if(time.ticks_ms() - debounceTime) > 500:
        buttonFlag3 = 1
        debounceTime=time.ticks_ms()

# Interrupt setup
#buttonPin0.irq(trigger=Pin.IRQ_FALLING, handler = button0Pressed)
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


    #check for the level to know how fast to itterate the buttons
    if level == 0:
        time.sleep(speed)

    if level == 1:
        time.sleep(speed)

    if level == 2:
        time.sleep(speed)

    if level == 3:
        time.sleep(speed)

    # turn off all LEDs
    ledPin0.off()
    ledPin1.off()
    ledPin2.off()
    ledPin3.off()

    #check if the correct button was pressed
    if buttonFlag0 == 1:
        buttonFlag0 = 0 #clear the interrupt
        Score = Score + 1
        print("Score: ", Score)

    if buttonFlag1 == 1:
        buttonFlag1 = 0 #clear the interrupt
        Score = Score + 1
        print("Score: ", Score)

    if buttonFlag2 == 1:
        buttonFlag2 = 0 #clear the interrupt
        Score = Score + 1
        print("Score: ", Score)

    if buttonFlag3 == 1:
        buttonFlag3 = 0 #clear the interrupt
        Score = Score + 1
        print("Score: ", Score)

    #check the score and decrease the speed to increase the level
    if Score == 10:
        speed = 1.75 
        print("you are on level 2")

    if Score == 20:
        speed = 1.5
        print("you are on level 3")

    if Score == 30:
        speed = 1.25
        print("you are on level 4")

    if Score == 40:
        speed = 1#last level of the game
        print("you are on level 5")

    if Score == 50:
        print("you passed the game!!")
        break