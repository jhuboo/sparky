#!/home/pi/spotmicroai/venv/bin/python3 -u

import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo as servo
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
pca9685_reference_clock_speed = int(Config().get(
    'motion_controller[*].boards[*].pca9685_1[*].reference_clock_speed | [0] | [0] | [0]'))
pca9685_frequency = int(
    Config().get('motion_controller[*].boards[*].pca9685_1[*].frequency | [0] | [0] | [0]'))

gpio_port = Config().get(Config.ABORT_CONTROLLER_GPIO_PORT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_port, GPIO.OUT)
GPIO.output(gpio_port, False)
time.sleep(1)

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus=i2c, address=pca9685_address, reference_clock_speed=pca9685_reference_clock_speed)
pca.frequency = pca9685_frequency

#input("Press Enter to do something: ")

servo_list = [8,9,10,12,13,14,4,5,6,0,1,2]
rest_angles = [75,100,0,105,80,180,105,100,0,75,80,180]
stand_angles = [75, 90, 90, 105, 90, 90, 105, 90, 90, 75, 90, 90]

def set_servo_angle(s, a):
    active_servo = servo.Servo(pca.channels[s])
    active_servo.set_pulse_width_range(min_pulse=500, max_pulse=2500)
    active_servo.angle=a

def init_servos():
    for x in range(len(servo_list)):
        set_servo_angle(servo_list[x], rest_angles[x])
        time.sleep(0.1)

def stand_straight():
    for x in range(len(servo_list)):
        set_servo_angle(servo_list[x], stand_angles[x])
        time.sleep(0.1)


if __name__=="__main__":
    try:
        while(True):
            init_servos()
            time.sleep(5)
            stand_straight()
            time.sleep(5)
    except:
        log.error("trouble connecting to the servos")
