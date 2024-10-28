# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""CircuitPython CPU temperature example in Celsius"""
import time
import microcontroller
import board
import digitalio

led = digitalio.DigitalInOut(board.IO33)
led.direction = digitalio.Direction.OUTPUT

while True:
    print(microcontroller.cpu.temperature)
    print("On!")
    led.value = True
    time.sleep(0.5)

    print("Off!")
    led.value = False
    time.sleep(0.5)
