
import board
import pwmio
import math
import simpleio
from analogio import AnalogIn
from time import sleep

potIn = board.IO2
pot = AnalogIn(potIn)

LED = board.IO4
led = pwmio.PWMOut(LED)

def converter(pin):
    pinValue = pin.value
    mapValue = math.trunc(simpleio.map_range
           	(pinValue, 536, 51355, 0, 65535))
    print('Valor Original: ', pinValue,
          'Valor Convertido: ', mapValue)
    return mapValue

while True:
    potValue = converter(pot)
    led.duty_cycle = potValue
    sleep(0.1)

