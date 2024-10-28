#Lição 1: Lição 1 - Hello World(Pisca LED)
import board
import time
from digitalio import DigitalInOut, Direction

# Configurando o pino do LED

# o led que configurei foi o pino 4 = IO4
led = DigitalInOut(board.IO4)
led.direction = Direction.OUTPUT

#loop infinito - executando sempre
while  True:
  led.value = True
  time.sleep(0.5)
  led.value = False
  time.sleep(0.5)

