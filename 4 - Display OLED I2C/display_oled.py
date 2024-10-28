import board
import busio
import adafruit_ssd1306
import time

i2c = busio.I2C(scl=board.IO9, sda=board.IO8)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

try:
 inverter = False
 while True:
   oled.invert(inverter)
   oled.fill(0)
   oled.rect(0, 0, 128, 64, 1)
   oled.rect(2, 2, 124, 60, 1)
   oled.text('Franzininho', 4, 4, 1)
   oled.text('WiFi', 4, 14, 1)
   oled.show()
   inverter = not inverter
   time.sleep(2)
finally:
 oled.invert(False)
 oled.fill(0)
 oled.show()

