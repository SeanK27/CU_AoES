# Desc: This file contains the pin definitions for the various components of the robot.

# Standard imports
from machine import PWM, Pin, ADC
##################

# User imports

##############

# Global Variable
controlMethod = 0   # 0 for IR, 1 for RF

# Pin Definitions

# Motor Pins
motor1Pin = 12
motor1PWMPin = 13
motor2Pin = 14
motor2PWMPin = 15

# Buzzer Pin
buzzerPin = 11

# IR Receiver Pin
irReceiverPin = 18

# IR Transmitter Pin
irTransmitterPin = 18

# RF Receiver Pin
rfReceiverPin0 = 7
rfReceiverPin1 = 6
rfReceiverPin2 = 5
rfReceiverPin3 = 4

######################

# Pin Class Configurations

# Motor PWM
motor1 = Pin(motor1Pin)
motor2 = Pin(motor2Pin)

# Buzzer ADC
buzzer = Pin(buzzerPin)

# IR Receiver Input
irReceiver = Pin(irReceiverPin, Pin.IN)

# IR Transmitter Output
irTransmitter = Pin(irTransmitterPin, Pin.OUT)

# RF Receiver Inputs
rfReceiver0 = Pin(rfReceiverPin0, Pin.IN)
rfReceiver1 = Pin(rfReceiverPin1, Pin.IN)
rfReceiver2 = Pin(rfReceiverPin2, Pin.IN)
rfReceiver3 = Pin(rfReceiverPin3, Pin.IN)