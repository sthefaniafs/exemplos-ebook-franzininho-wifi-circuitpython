#Leitura de Entrada analógica -  Exemplo 1
import time            #importa módulo de temporização
import board            #importa módulo da placa
from analogio import AnalogIn    #immport módulo de entrada analógica

analog_in = AnalogIn(board.IO1) #mapeia pino analógico

while True:             #loop infinito
   print((analog_in.value,))    #imprime o valor da leitura analógica
   time.sleep(0.2)         #aguarda 200 ms

