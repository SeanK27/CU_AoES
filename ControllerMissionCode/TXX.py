import time
from ir_tx.nec import NEC
from machine import Pin

tx_pin = Pin(18,Pin.OUT,value=0)
device_addr = 0x12
transmitter = NEC(tx_pin)

commands = [0x11,0x12,0x13,0x14]

if __name__ == "__main__":
  while True:
    for command in commands:
      transmitter.transmit(device_addr,command)
      print("COMMANDS",hex(command),"TRANSMITTED.")
      time.sleep(1)