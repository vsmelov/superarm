import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
#FREQ = 50*1000
FREQ = 50
MOTORS_PINS = [17, 18, 27, 22, 23, 24]
motors = {}
DELAY = 3
START_POSITION = 50

motors_inited = set()


#motor, position: 0 10
#motor, position: 1 10
#init motor 1
#motor, position: 1 5
#motor, position: 1 7
#motor, position: 2 5
#init motor 2
#motor, position: 2 10
#motor, position: 3 10
#init motor 3
#motor, position: 3 70
#motor, position: 4 10
#init motor 4
#motor, position: 4 50
#motor, position: 4 30
#motor, position: 4 90
#motor, position: 4 20
#motor, position: 5 50
#init motor 5
#motor, position: 



def ensure_motor(motor_index, pos):
	if motor_index not in motors_inited:
		print('init motor {}'.format(motor_index))
		pin = MOTORS_PINS[motor_index]
		GPIO.setup(pin, GPIO.OUT)
		motors_inited.add(motor_index)
		p = GPIO.PWM(pin, FREQ)
		p.start(0)
		motors[motor_index] = p
	motors[motor_index].ChangeDutyCycle(pos)


while True:
	com = input('motor, position: ')
	motor_index = int(com.split()[0])
	position = float(com.split()[1])
	ensure_motor(motor_index, position)

p.stop()
GPIO.cleanup()
