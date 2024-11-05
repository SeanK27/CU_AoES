import machine
from machine import I2C, Pin, PWM
import seesaw
import time
import seesaw

# Initialize I2C. Adjust pin numbers based on your Pico's configuration
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Initialize the Seesaw driver with the I2C interface
# Use the Gamepad QT's I2C address from the Arduino code (0x50)
seesaw_device = seesaw.Seesaw(i2c, addr=0x50)

pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT) # Initialize GP14 as an OUTPUT
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)
pwm = min(max(int(2**16 * abs(1)), 0), 65535)

ain3_ph = Pin(10, Pin.OUT) # Initialize GP14 as an OUTPUT
ain4_en = PWM(11, freq = pwm_rate, duty_u16 = 0)
pwm1 = min(max(int(2**16 * abs(1)), 0), 65535)

# Define button and joystick pin numbers as per the Arduino code
BUTTON_A = 5
BUTTON_B = 1
BUTTON_X = 6
BUTTON_Y = 2
BUTTON_START = 16
BUTTON_SELECT = 0
JOYSTICK_X_PIN = 14
JOYSTICK_Y_PIN = 15

# Button mask based on Arduino code
BUTTONS_MASK = (1 << BUTTON_X) | (1 << BUTTON_Y) | \
              (1 << BUTTON_A) | (1 << BUTTON_B) | \
              (1 << BUTTON_SELECT) | (1 << BUTTON_START)

# Define LED pins
LED_1_PIN = 12
LED_2_PIN = 13
LED_3_PIN = 15
LED_4_PIN = 14

# Initialize LED states
led_states = {
   BUTTON_A: False,
   BUTTON_B: False,
   BUTTON_X: False,
   BUTTON_Y: False,
   BUTTON_START: False,
   BUTTON_SELECT: False
}

# Initialize last button states
last_buttons = 0

# Initialize joystick center position
joystick_center_x = 507
joystick_center_y = 516

def setup_buttons():
   """Configure the pin modes for buttons."""
   seesaw_device.pin_mode_bulk(BUTTONS_MASK, seesaw_device.INPUT_PULLUP)

def read_buttons():
   """Read and return the state of each button."""
   return seesaw_device.digital_read_bulk(BUTTONS_MASK)

def set_led(pin, state):
   """Turn the LED connected to the given pin on or off."""
   pin.value(state)

def handle_button_press(button):
   """Toggle the corresponding LED state on button press."""
   global led_states
   led_states[button] = not led_states[button]
   if button == BUTTON_A:
       set_led(Pin(LED_1_PIN, Pin.OUT), led_states[button])
   elif button == BUTTON_B:
       set_led(Pin(LED_2_PIN, Pin.OUT), led_states[button])
   elif button == BUTTON_X:
       set_led(Pin(LED_3_PIN, Pin.OUT), led_states[button])
   elif button == BUTTON_Y:
       set_led(Pin(LED_4_PIN, Pin.OUT), led_states[button])
   print("Button", button, "is", "pressed" if led_states[button] else "released")

# Motor 1 Control
def motor1ONDirForward():
    print("motor on")
    ain1_ph.high()
    ain2_en.duty_u16(pwm)

def motor1OFF():
    print("motor off")
    ain2_en.duty_u16(0)

def motor1ONDirBackward():
    print("motor toggle")
    ain1_ph.low()
    ain2_en.duty_u16(pwm)
    
    
# Motor 2 Control
def motor2ONDirForward():
    print("motor on")
    ain3_ph.high()
    ain4_en.duty_u16(pwm1)

def motor2OFF():
    print("motor off")
    ain4_en.duty_u16(0)
    
def motor2ONDirBackward():
    print("motor toggle")
    ain3_ph.low()
    ain4_en.duty_u16(pwm1)

def main():
   """Main program loop."""
   global last_buttons  # Ensure last_buttons is recognized as a global variable

   setup_buttons()

   last_x, last_y = seesaw_device.analog_read(JOYSTICK_X_PIN), seesaw_device.analog_read(JOYSTICK_Y_PIN)
   joystick_threshold = 150  # Adjust threshold as needed
   
   motor1OFF()
   motor2OFF()

   while True:
       current_buttons = read_buttons()

       # Check if button state has changed
       for button in led_states:
           if current_buttons & (1 << button) and not last_buttons & (1 << button):
               handle_button_press(button)

       # Read joystick values
       current_x = seesaw_device.analog_read(JOYSTICK_X_PIN)
       current_y = seesaw_device.analog_read(JOYSTICK_Y_PIN)
       
       motor1OFF()
       motor2OFF()

       # Check if joystick position has changed significantly
       if abs(current_x - last_x) > joystick_threshold or abs(current_y - last_y) > joystick_threshold:
           print("Joystick moved - X:", current_x, ", Y:", current_y)
           last_x, last_y = current_x, current_y

           # Determine which LED to turn on based on joystick direction
           if current_y < joystick_center_y - joystick_threshold:  # Joystick moved up
               motor1ONDirForward()
               motor2ONDirForward()
           elif current_y > joystick_center_y + joystick_threshold:  # Joystick moved down
               motor1ONDirBackward()
               motor2ONDirBackward()
           elif current_x < joystick_center_x - joystick_threshold:  # Joystick moved left
               motor1ONDirForward()
               motor2ONDirBackward()
           elif current_x > joystick_center_x + joystick_threshold:  # Joystick moved right
               motor1ONDirBackward()
               motor2ONDirForward()

       last_buttons = current_buttons
       time.sleep(0.1)  # Delay to prevent overwhelming the output

if __name__ == "__main__":
   main()
