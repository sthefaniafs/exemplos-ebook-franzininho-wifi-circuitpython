# Entradas e Saídas digitais - Botão Liga/Desliga
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# Configura o pino do botão
btn = DigitalInOut(board.IO5)      	# mapea para pino 5
btn.direction = Direction.INPUT  	# configura como entrada
btn.pull = Pull.UP                  # habilita pull-up interno


# Configura o pino do led
led = DigitalInOut(board.IO4)       # mapea para pino 4
led.direction = Direction.OUTPUT   	# configura como saída

# loop infinito
while True:
	if btn.value ==0:			   	# Se botão pressionado
		led.value=not led.value		# inverte estado do LED
		while btn.value==0:			# Aguarda botão ser solto
			time.sleep(0.01)		# delay de 10 ms

