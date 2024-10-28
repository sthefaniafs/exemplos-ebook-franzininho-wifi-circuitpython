# code.py

""" Controle da cor do LED RGB através da serial console """
import board
import digitalio
import neopixel_write

pin = digitalio.DigitalInOut(board.NEOPIXEL)
pin.direction = digitalio.Direction.OUTPUT

while True:
   print("Digite a intesidade da cor vermelho:")
   r = int(input())
   print("Digite a intesidade da cor verde:")
   g = int(input())
   print("Digite a intesidade da cor azul:")
   b = int(input())
   cor = bytearray([r, g, b])
   neopixel_write.neopixel_write(pin, cor)
   print("Cor: {} {} {}".format(r,g,b) )
   print("[ENTER] - para mudar a cor.")
   input()

