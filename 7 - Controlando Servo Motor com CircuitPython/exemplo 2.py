
import board
import pwmio
from adafruit_motor import servo
import simpleio
import math
from analogio import AnalogIn
from time import sleep

pin = board.IO1
pwm = pwmio.PWMOut(pin, frequency = 50)
my_servo = servo.Servo(pwm)

potPin = board.IO2
pot = AnalogIn(potPin)

def converter(pin):
    pinValue = pin.value
    mapValue = math.trunc(simpleio.map_range
           	(pinValue, 536, 51355, 0, 180))
    return mapValue

while True:
    angle = converter(pot)
    my_servo.angle = angle
    sleep(0.1)

