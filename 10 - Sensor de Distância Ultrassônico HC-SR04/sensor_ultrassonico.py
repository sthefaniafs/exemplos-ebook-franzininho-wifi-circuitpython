import board
import time
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.IO36, echo_pin=board.IO35, timeout=0.5)

while True:
   try:
       print((sonar.distance,))
   except RuntimeError:
       print("Retrying!")
   time.sleep(0.1)

