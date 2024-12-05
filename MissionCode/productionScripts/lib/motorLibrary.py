# Desc: This file contains the motor control functions for the robot.

# Standard imports
from machine import PWM, Pin, ADC
##################

# User imports
from lib import pinDefinitions
##############

# Motor 1 PWM Define
motor1PWM = PWM(pinDefinitions.motor1PWMPin, freq = 2000, duty_u16 = 0)

# Motor 2 PWM Define
motor2PWM = PWM(pinDefinitions.motor2PWMPin, freq = 2000, duty_u16 = 0)


# Motor Control
def motorONForward(speed):
    print("motors on forward")
    pinDefinitions.motor1.high()
    pinDefinitions.motor2.high()
    motor1PWM.duty_u16(speed)
    motor2PWM.duty_u16(speed)
    
    """
    This function turns on both motors in the forward direction given a speed.
    speed: the speed of the motor from 0 - 65535 for the PWM signal
    """

def motorONBackward(speed):
    print("motors on backward")
    pinDefinitions.motor1.low()
    pinDefinitions.motor2.low()
    motor1PWM.duty_u16(speed)
    motor2PWM.duty_u16(speed)
    
    """
    This function turns on both motors in the backward direction given a speed.
    speed: the speed of the motor from 0 - 65535 for the PWM signal
    """

def motorOFF():
    print("motors off")
    motor1PWM.duty_u16(0)
    motor2PWM.duty_u16(0)
    
    """
    This function turns off both motors.
    """

def motorONLeft(speed):
    print("motors on left")
    pinDefinitions.motor1.low()
    pinDefinitions.motor2.high()
    motor1PWM.duty_u16(0)               #FIXME
    motor2PWM.duty_u16(speed)
    
    """
    This function turns on the left motor in the backward direction and the right motor in the forward direction given a speed.
    speed: the speed of the motor from 0 - 65535 for the PWM signal
    """

def motorONRight(speed):
    print("motors on right")
    pinDefinitions.motor1.high()
    pinDefinitions.motor2.low()
    motor1PWM.duty_u16(speed)
    motor2PWM.duty_u16(0)               #FIXME
    
    """
    This function turns on the left motor in the forward direction and the right motor in the backward direction given a speed.
    speed: the speed of the motor from 0 - 65535 for the PWM signal
    """

# Motor Drive
def motorDrive(direction, speed):
    if direction == "Forward":
        motorONForward(speed)
    elif direction == "Backward":
        motorOFF()                  #FIXME
    elif direction == "Left":
        motorONLeft(speed + 3000)
    elif direction == "Right":
        motorONRight(speed)
    else:
        motorOFF()
    
    """
    This function drives the robot in the specified direction at the specified speed.
    direction: the direction in which the robot should move
    speed: the speed of the robot from 0 - 65535 for the PWM signal
    """
