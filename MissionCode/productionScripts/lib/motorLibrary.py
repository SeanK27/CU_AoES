# Desc: This file contains the pin definitions for the various components of the robot.

# Standard imports
from machine import PWM, Pin, ADC
##################

# User imports
from lib import pinDefinitions
##############

# Motor 1 PWM Define
motor1PWM = PWM(pinDefinitions.motor1Pin, freq = 2000, duty_u16 = 0)

# Motor 2 PWM Define
motor2PWM = PWM(pinDefinitions.motor2Pin, freq = 2000, duty_u16 = 0)


# Motor 1 Control
def motor1ONDirForward(speed):
    print("motor on")
    pinDefinitions.motor1.high()
    motor1PWM.duty_u16(speed)

    """
    This function turns on motor 1 in the forward direction given a speed.
    speed: the speed of the motor from 0 - 65535 for the PWM signal
    """

def motor1OFF():
    print("motor off")
    motor1PWM.duty_u16(0)
    
    """
    This function turns off motor 1.
    """

def motor1ONDirBackward(speed):
    print("motor toggle")
    pinDefinitions.motor1.low()
    motor1PWM.duty_u16(speed)
    
    """
    This function turns on motor 1 in the backward direction given a speed.
    speed: the speed of the motor from 0 - 65535 for the PWM signal
    """
#################
    
    
# Motor 2 Control
def motor2ONDirForward(speed):
    print("motor on")
    pinDefinitions.motor2.high()
    motor2PWM.duty_u16(speed)
    
    """
    This function turns on motor 2 in the forward direction given a speed.
    speed: the speed of the motor from 0 - 65535 for the PWM signal
    """

def motor2OFF():
    print("motor off")
    motor2PWM.duty_u16(0)
    
    """
    This function turns off motor 2.
    """
    
def motor2ONDirBackward(speed):
    print("motor toggle")
    pinDefinitions.motor2.low()
    motor2PWM.duty_u16(speed)
    
    """
    This function turns on motor 2 in the backward direction given a speed.
    speed: the speed of the motor from 0 - 65535 for the PWM signal
    """
#################