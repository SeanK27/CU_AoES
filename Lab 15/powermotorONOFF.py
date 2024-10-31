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

ain3_ph = Pin(10, Pin.OUT) # Initialize GP14 as an OUTPUT
ain4_en = PWM(11, freq = pwm_rate, duty_u16 = 0)
pwm1 = min(max(int(2**16 * abs(1)), 0), 65535)

# Motor 1 Control
def motor1ON():
    print("motor on")
    ain1_ph.low()
    ain2_en.duty_u16(pwm)


def motor1OFF():
    print("motor off")
    ain1_ph.high()
    ain2_en.duty_u16(0)


def motor1Toggle():
    print("motor toggle")
    ain1_ph.toggle()
    ain2_en.duty_u16(pwm)
    
# Motor 2 Control
def motor2ON():
    print("motor on")
    ain3_ph.low()
    ain4_en.duty_u16(pwm1)

def motor2OFF():
    print("motor off")
    ain3_ph.high()
    ain4_en.duty_u16(0)
    
def motor2Toggle():
    print("motor toggle")
    ain3_ph.toggle()
    ain4_en.duty_u16(pwm1)



while True:
    motor1ON()
    motor2ON()

    # time.sleep(1)

    # motor1OFF()
    # motor2OFF()

    # time.sleep(1)