# Desc: This file contains the pin definitions for the various components of the robot.

# Standard imports
from machine import PWM, Pin, ADC
##################

# User imports

##############


# Pin Definitions

# Motor Pins
motor1Pin = 17
motor2Pin = 18

# Buzzer Pin
buzzerPin = 27

# IR Receiver Pin
irReceiverPin = 14

# IR Transmitter Pin
irTransmitterPin = 13

# RF Receiver Pin
rfReceiverPin0 = 12
rfReceiverPin1 = 15
rfReceiverPin2 = 16
rfReceiverPin3 = 19

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