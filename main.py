# Created by: Jack Eddy
# Created on: March 2025
#
# This program turns the LED on the pico on and off, increasing the time the light stays on each cycle

import time
import board
import digitalio

# variables
blink_time = 1

# sets LED pin to output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# runs loop turning LED on for set time and off for set time, increases every cycle
while True:
    led.value = True
    time.sleep(blink_time)
    led.value = False
    time.sleep(blink_time)
    blink_time += 1