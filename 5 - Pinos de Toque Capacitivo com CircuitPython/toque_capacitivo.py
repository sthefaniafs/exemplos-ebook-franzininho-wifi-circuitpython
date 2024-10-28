# Toque Capacitivo
import board
import touchio
from digitalio import DigitalInOut, Direction
from time import sleep

estado = 0

pin = board.IO1
touch = touchio.TouchIn(pin)

led = DigitalInOut(board.IO4)
led.direction = Direction.OUTPUT

while True:
    if touch.value:
        estado = not estado

    led.value = estado
    sleep(1)

