import math, time
# load the MicroPython pulse-width-modulation module for driving hardware
from machine import PWM, Pin, ADC
import productionScripts.lib.buzzerLibrary as buzzerLibrary

# Pin objects
ADCPin = Pin(27)

# ADC objects
batteryADC = ADC(ADCPin)

# PWM objects
# buzzer = PWM(Pin(13))
# buzzer.freq(440)            # 440 Hz
# buzzer.duty_u16(30000)      # 100% duty cycle


while True:
    batteryVoltage = batteryADC.read_u16() * 3.3 / 65535
    print("Battery Voltage: ", batteryVoltage)

    buzzerLibrary.buzzerOn(Pin(12), 440, 30000)