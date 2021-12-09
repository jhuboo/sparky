#!/home/pi/spotmicroai/venv/bin/python3 -u

import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from pick import pick
import time
import os
import sys
import RPi.GPIO as GPIO
from spot_micro_kinematics_python.spot_micro_stick_figure import SpotMicroStickFigure

from spotmicroai.utilities.log import Logger
from spotmicroai.utilities.config import Config

log = Logger().setup_logger('Powering up SPARKY!')

log.info('setup')

pca=None
pca9685_address = 0x40
pca9685_reference_clock_speed = 25000000
pca9685_frequency = 50

gpio_port = Config().get(Config.ABORT_CONTROLLER_GPIO_PORT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_port, GPIO.OUT)
GPIO.output(gpio_port, False)
time.sleep(1)

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus=i2c, address=pca9685_address, reference_clock_speed=pca9685_reference_clock_speed)
pca.frequency = pca9685_frequency

#input("Press Enter to do something: ")

def init_spot(): 
    spot = SpotMicroStickFigure()
    spot.print_leg_angles()

init_spot()

servo_list = [8,9,10,12,13,14,4,5,6,0,1,2]
rest_angles = [75,100,0,105,80,180,105,100,0,75,80,180]

for x in range(len(servo_list)):
    active_servo = servo.Servo(pca.channels[servo_list[x]])
    active_servo.set_pulse_width_range(min_pulse=500, max_pulse=2500)
    active_servo.angle=rest_angles[x]
    time.sleep(0.1)