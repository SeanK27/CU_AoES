# Standard imports
import time
from machine import PWM, Pin, ADC
##################

# User imports
from lib import pinDefinitions
from lib import buzzerLibrary
from lib import motorLibrary
from lib import RFLibrary
from lib import joystickLibrary
##############

# Mode Setup

RFLibrary.RFEnable()    # Set the control method to RF


# Mission Loop
while True:

    while pinDefinitions.controlMethod == 1:        # RF is activated
        
        # Get the direction from the RF controller
        direction = RFLibrary.RFGetDir()
        
        # Move the robot in the direction
        motorLibrary.motorDrive(direction, 65535)       # Full speed