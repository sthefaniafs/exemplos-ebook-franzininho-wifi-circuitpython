#Leitura de Entrada analógica - Exemplo 3
import time            #importa módulo de temporização
import board            #importa módulo da placa
from analogio import AnalogIn    #immport módulo de entrada analógica
from digitalio import DigitalInOut, Direction

analog_in = AnalogIn(board.IO1) #mapeia pino analógico

led = DigitalInOut(board.IO4)
led.direction = Direction.OUTPUT

def ler_tensao(pin):
   return (pin.value * 3.3) / 65536

while True:             #loop infinito
   print((ler_tensao(analog_in),))    #imprime o valor da leitura analógica

   if(ler_tensao(analog_in)>2.5):      #se valor lido for maior que 2.5V
       led.value = 1               #liga LED
   else:                   #se não
       led.value =0               #desliga o LED

   time.sleep(0.2)         #aguarda 200 ms

