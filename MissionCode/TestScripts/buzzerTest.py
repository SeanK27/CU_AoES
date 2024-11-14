import math, time
# load the MicroPython pulse-width-modulation module for driving hardware
from machine import PWM, Pin, ADC
import MissionCode.productionScripts.lib.buzzerLibrary as buzzerLibrary

# Pin objects
ADCPin = Pin(27)

# ADC objects
batteryADC = ADC(ADCPin)

# PWM objects
buzzer = PWM(Pin(12))


while True:
    batteryVoltage = batteryADC.read_u16() * 3.3 / 65535
    print("Battery Voltage: ", batteryVoltage)

    buzzerLibrary.buzzerOn(buzzer, 440, 30000)
    
    time.sleep(5)
    
    buzzerLibrary.buzzerOff(buzzer)