import math, time
# load the MicroPython pulse-width-modulation module for driving hardware
from machine import PWM, Pin, ADC


def buzzerOn(buzzer, freq, duty):
    buzzer.freq(440)            # 440 Hz
    buzzer.duty_u16(30000)      # 50% duty cycle
    
    """
    This function turns on the buzzer with the specified frequency and duty cycle.
    buzzer: the buzzer object
    freq: the frequency of the buzzer in Hz
    duty: the duty cycle of the buzzer out of 65535 for volume (dont go above 35000)
    """

# FIXME: I have no clue why this doesn't shut off the buzzer. No need to shut off if BVM triggers though.
def buzzerOff(buzzer):
    buzzer.deinit()
    
    """
    This function turns off the buzzer.
    buzzer: the buzzer object
    """

# Buzzer siren method (1500Hz to 1980Hz and back)
def buzzerSiren(pin, freq):
    
    buzzer = PWM(pin)
    
    for freq in range(1500, 1980, 25):
        buzzer.freq(freq)
        time.sleep(0.01)
        
    for freq in range(1980, 1500, -25):
        buzzer.freq(freq)
        time.sleep(0.01)
        
    """
    This function creates a siren sound by varying the frequency of the buzzer from 1500Hz to 1980Hz and back.
    WARNING: This will hang the system until the siren is complete. Probably a bad idea to use this.
    pin: the pin number to which the buzzer is connected
    freq: the frequency of the buzzer in Hz
    """