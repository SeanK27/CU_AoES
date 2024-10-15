import machine
import ir_tx
from machine import Pin
import uasyncio as asyncio
from ir_tx.nec import NEC

# Define an asynchronous function to handle IR transmission
async def transmit_ir():
    ir_transmitter = NEC(Pin(17, Pin.OUT, value=0)) # Initialize IR transmitter on Pin 17
    addr = 0x02 # Device Address

    commands = [0x01, 0x02, 0x03, 0x04] # List of data to send
 
    while True:
        for command in commands:
            ir_transmitter.transmit(addr, command)      # Send each command
            print(f"IR signal transmitted: Addr {addr}, Command {command}")     # Print The transmitted command
            await asyncio.sleep(3)      # Wait for 3 seconds before sending the next command
            
# Main function to run the transmitter
async def main():
    await transmit_ir() # Call the transmit function

if __name__ == "__main__":
    asyncio.run(main()) # Start the asynchronous event loop