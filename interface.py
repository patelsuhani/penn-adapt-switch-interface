# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# Modified by: Loreto Dumitrescu
# CircuitPython code for the Rocket Switch Interface designed by Milad from Makers Making Change. 
# Project Details: https://makersmakingchange.com/project/rocket-switch-interface/

"""CircuitPython Rocket Switch Interface- Keyboard"""
import time
import board
import digitalio
# import analogio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Initialize the constants for voltage options of switch

ENTER_VOLTAGE = 0.019
SPACE_VOLTAGE = 1.6
CLICK_VOLTAGE = 3.322

SWITCH_TOLERANCE = 0.4

# Set Power pin
power_pin = digitalio.DigitalInOut(board.ROTB)
power_pin.direction = digitalio.Direction.OUTPUT
power_pin.value = True

# The make the SWITCH pin a digital input pin with internal pullup

digital_button_pin = digitalio.DigitalInOut(board.SWITCH)
digital_button_pin.direction = digitalio.Direction.INPUT
digital_button_pin.pull = digitalio.Pull.DOWN


# Analog pin that's used for the toggle switch
# analog_switch_pin = analogio.AnalogIn(board.ROTA)
# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# Creates an instance of the on board light and sets it as an output
led = digitalio.DigitalInOut(board.NEOPIXEL)
led.direction = digitalio.Direction.OUTPUT

print("Waiting for key pin...")

while True:
    # Check analog switch Value
    # switch_val = analog_switch_pin.value

    # # If switch value = option 1 -> key_out = ENTER
    # if switch_val >= ENTER_VOLTAGE - SWITCH_TOLERANCE and switch_val <= ENTER_VOLTAGE + SWITCH_TOLERANCE:
    #     key_out = Keycode.ENTER

    # # If switch value = option 2 -> key_out = SPACE
    # elif switch_val >= SPACE_VOLTAGE - SWITCH_TOLERANCE and switch_val <= SPACE_VOLTAGE + SWITCH_TOLERANCE:
    #     key_out = Keycode.SPACE

    # # If switch value = option 3 -> key_out = LEFT_BUTTON
    # elif switch_val >= CLICK_VOLTAGE - SWITCH_TOLERANCE and switch_val <= CLICK_VOLTAGE + SWITCH_TOLERANCE:
    #     key_out = Mouse.LEFT_BUTTON
    
    # else:
    #     key_out = Keycode.SPACE
    key_out = Keycode.SPACE
    # Check each pin
    if digital_button_pin.value:  # Is it grounded?
        
        print("Pin switch is grounded.")
        
        # Turn on the red LED
        led.value = True

        while digital_button_pin.value:
            pass  # Wait for it to be ungrounded!            
        keyboard.press(key_out)  # "Press"...
        keyboard.release_all()  # ..."Release"!
        # Turn off the red LED
        led.value = False

    time.sleep(0.01)
