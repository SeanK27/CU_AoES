from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(13)) # Set the pin for the PWM object
pwm1 = PWM(Pin(12))
pwm2 = PWM(Pin(11))




pwm.freq(60) # Set the frequency of the PWM signal

#dim the LED over time
while True:

    for duty in range(65025):
        pwm1.duty_u16(duty)
        pwm2.duty_u16(duty)
        pwm.duty_u16(duty)
        sleep(0.00001)
        print(duty)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        pwm1.duty_u16(duty)
        pwm2.duty_u16(duty)
        sleep(0.00001)
        print(duty)
