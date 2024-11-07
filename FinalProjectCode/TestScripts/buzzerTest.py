import math, time
import machine
# load the MicroPython pulse-width-modulation module for driving hardware
from machine import PWM, Pin, ADC

# ADC objects
batteryADC = ADC(Pin(32))

# PWM objects
buzzer = PWM(Pin(13))
buzzer.freq(440)            # 440 Hz
buzzer.duty_u16(30000)      # 100% duty cycle


while True:
    batteryVoltage = batteryADC.read_u16() * 3.3 / 65535
    print("Battery Voltage: ", batteryVoltage)

    # A siren from 1500Hz to 1980Hz and back
    for freq in range(1500, 1980, 25):
        buzzer.freq(freq)
        time.sleep(0.01)
    for freq in range(1980, 1500, -25):
        buzzer.freq(freq)
        time.sleep(0.01)