import board
import time

from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn

relay = DigitalInOut(board.IO0)
relay.switch_to_output()

humid_analog = AnalogIn(board.IO1)
humid_digital = DigitalInOut(board.IO4)
humid_digital.direction = Direction.INPUT

relay.value = True

wait_time = 1
watering_time = 1

dry_value = 51130

while True:
   try:
       print("humid (Digital value):", humid_digital.value)
       print("humid (Analogic value):", humid_analog.value)

       time.sleep(1);

       if humid_analog.value > dry_value :
           print("Starting watering...")

           relay.value = False

           time.sleep(watering_time)
           print("Finishing watering.")

       else:
           relay.value = True
           time.sleep(wait_time)

   except RuntimeError as e:
       print("Read failure")

   time.sleep(1)

