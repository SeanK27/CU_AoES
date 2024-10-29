import math, time
import machine
# load the MicroPython pulse-width-modulation module for driving hardware
from machine import PWM
from machine import Pin


time.sleep(1) # Wait for USB to become ready


pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT) # Initialize GP14 as an OUTPUT
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)
pwm = min(max(int(2**16 * abs(1)), 0), 65535)


def motorON():
    print("motor on")
    ain1_ph.low()
    ain2_en.duty_u16(pwm)


def motorOFF():
    print("motor off")
    ain1_ph.high()
    ain2_en.duty_u16(0)


def motorToggle():
    print("motor toggle")
    ain1_ph.toggle()
    ain2_en.duty_u16(pwm)



while True:
    motorON()

    time.sleep(1)

