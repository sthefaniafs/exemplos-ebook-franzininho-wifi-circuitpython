import board
import pwmio
from adafruit_motor import servo
from time import sleep

pin = board.IO1
pwm = pwmio.PWMOut(pin, frequency = 50)
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 10):
        my_servo.angle = angle
        sleep(0.1)
    for angle in range(180, 0, -10):
        my_servo.angle = angle
        sleep(0.1)

