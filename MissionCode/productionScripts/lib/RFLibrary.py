# Desc: This file contains the motor control functions for the robot.

# Standard imports
from machine import PWM, Pin, ADC
##################

# User imports
from lib import pinDefinitions
##############

def RFEnable():
    controlMethod = 1
    
    """
    Enables control with the RF
    """

def RFDisable():
    controlMethod = 0
    
    """
    Disables control with the RF
    """

def RFGetDir():
    
    # Read the state of each pin on the reciever.
    if pinDefinitions.rfReceiver0.value() == 1:
        return "Forward"
    if pinDefinitions.rfReceiver1.value() == 1:
        return "Backward"
    if pinDefinitions.rfReceiver1.value() == 1:
        return "Right"
    if pinDefinitions.rfReceiver1.value() == 1:
        return "Left"
    
    """
    Checks which button is pressed on the RF controller and returns a corresponding value.
    
    Returns:
    "Forward" if the A button is pressed
    "Backward" if the D button is pressed
    "Right" if the B button is pressed
    "Left" if the C button is pressed
    """