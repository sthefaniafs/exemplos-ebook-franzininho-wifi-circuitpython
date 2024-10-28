#Leitura de Entrada analógica - Exemplo 2
import time            #importa módulo de temporização
import board            #importa módulo da placa
from analogio import AnalogIn    #import módulo de entrada analógica

analog_in = AnalogIn(board.IO1) #mapeia pino analógico

def ler_tensao(pin):
   return (pin.value * 3.3) / 65536

while True:             #loop infinito
   print((ler_tensao(analog_in),))    #imprime o valor da leitura analógica
   time.sleep(0.2)         #aguarda 200 ms

