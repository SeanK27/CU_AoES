# Standard imports
import time
from machine import PWM, Pin, ADC
##################

# User imports
from lib import pinDefinitions
from lib import buzzerLibrary
from lib import motorLibrary
from lib import RFLibrary
from lib import IRRXLibrary
##############

# Mode Setup

controlMethod = 0       # 0 = IR, 1 = RF

direction = "a"

boost = 1

commands = [0x21,0x22,0x23,0x24,0x25, 0x26]
# FWD, BWD, LEFT, RIGHT, BOOST, STOP


# Mission Loop
while True:

    while controlMethod == 1:        # RF is activated
        
        # Get the direction from the RF controller
        # Read the state of each pin on the reciever.
        if pinDefinitions.rfReceiver3.value() == 1:
            direction = "Forward"
        if pinDefinitions.rfReceiver2.value() == 1:
            direction = "Backward"
        if pinDefinitions.rfReceiver0.value() == 1:
            direction = "Right"
        if pinDefinitions.rfReceiver1.value() == 1:
            direction = "Left"
        
        print(direction)
        
        # Move the robot in the direction
        if direction == "Forward":
            motorLibrary.motorDrive(direction, 10000)
        if direction == "Left":
            motorLibrary.motorDrive(direction, 10000)
        if direction == "Right":
            motorLibrary.motorDrive(direction, 10000)
        if direction == "Backward" and boost == 1:
            motorLibrary.motorDrive("Forward", 65535)
            time.sleep(0.5)
            boost = 0
        if direction == "Backward" and boost == 0:
            motorLibrary.motorDrive(direction, 0)
        
    while controlMethod == 0:        # IR is activated
        
        # Get the direction from the RF controller
        # Read the state of each pin on the reciever.
        if IRRXLibrary.IRGetData() == commands[0]:
            direction = "Forward"
        if IRRXLibrary.IRGetData() == commands[1]:
            direction = "Backward"
        if IRRXLibrary.IRGetData() == commands[2]:
            direction = "Right"
        if IRRXLibrary.IRGetData() == commands[3]:
            direction = "Left"
        if IRRXLibrary.IRGetData() == commands[4]:
            direction = "Forward"
            boost = 1
        if IRRXLibrary.IRGetData() == commands[5]:
            direction = "Backward"
        
        print(direction)
        
        # Move the robot in the direction
        if direction == "Forward":
            motorLibrary.motorDrive(direction, 10000)
        if direction == "Left":
            motorLibrary.motorDrive(direction, 10000)
        if direction == "Right":
            motorLibrary.motorDrive(direction, 10000)
        if direction == "Forward" and boost == 1:
            motorLibrary.motorDrive("Forward", 65535)
            time.sleep(0.5)
            boost = 0
        if direction == "Backward" and boost == 0:
            motorLibrary.motorDrive(direction, 0)