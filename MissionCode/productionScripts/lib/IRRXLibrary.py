# Desc: This file contains the motor control functions for the robot.

# Standard imports
from machine import PWM, Pin, ADC, I2C
import time
##################

# User imports
from lib import pinDefinitions
import ir_rx
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error
##############

IRData = 0

# Interrupt function to execute when an IR signal is received
def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: {data}, Addr: {addr}")

    IRSetData(data, addr)
    
def IRSetData(data, addr):
    
    # Store the received data
    IRData = data
    
    # Return the received data
    IRGetData()
    
def IRGetData():
    
    print("Successfully stored data!")
    
    # Return the received data
    return IRData
    
    
# Setup the IR receiver
ir_pin = Pin(18, Pin.IN, Pin.PULL_UP)                   # Initialize the GPIO Pin
ir_receiver = NEC_8(ir_pin, callback=ir_callback)       # Initialize the IR receiver and assign the GPIO Pin

# Print an error when thrown
ir_receiver.error_function(print_error)

# Main loop
while True:
    pass        # Execution is interrupt-driven, so just keep the script alive
    # print("Test")