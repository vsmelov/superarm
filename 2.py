from RPIO import PWM, GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
MOTORS_PINS = [17, 18, 27, 22, 23, 24]
motors = {}

motors_inited = set()


def init_motor(motor_index):
	print('init motor {}'.format(motor_index))
	pin = MOTORS_PINS[motor_index]
	servo = PWM.servo(dma_channel=motor_index)
	motors_inited.add(motor_index)
	motors[motor_index] = servo


def ensure_motor(motor_index, pos):
	if motor_index not in motors_inited:
		init_motor(motor_index)
	pin = MOTORS_PINS[motor_index]
	motors[motor_index].set_servo(pin, pos)


while True:
	com = input('motor, position: ')
	motor_index = int(com.split()[0])
	position = float(com.split()[1])
	ensure_motor(motor_index, position)
