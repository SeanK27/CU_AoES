import ir_rx
import machine
from machine import Pin
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error

# Interrupt function to execute when an IR signal is received
def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")

# Setup the IR receiver
ir_pin = Pin(17, Pin.IN, Pin.PULL_UP)                   # Initialize the GPIO Pin
ir_receiver = NEC_8(ir_pin, callback=ir_callback)       # Initialize the IR receiver and assign the GPIO Pin

# Print an error when thrown
ir_receiver.error_function(print_error)

# Main loop
while True:
    pass        # Execution is interrupt-driven, so just keep the script alive
    # print("Test")