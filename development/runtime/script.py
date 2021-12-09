#!/home/pi/spotmicroai/venv/bin/python3 -u

import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo as servo
from pick import pick
import time
from math import pi
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

#order: 
# rear_left: 8, 9, 10(shoulder, leg, feet), = 0, 1, 2
# rear_right: 12, 13, 14                    = 3, 4, 5
# front_left: 4, 5, 6                       = 6, 7, 8
# front_right: 0, 1, 2                      = 9, 10, 11
servos = [(8,90),(9,90),(10,90),(12,90),(13,90),(14,90),(4,90),(5,90),(6,90),(0,90),(1,90),(2,90)]
rest_angles = [75,100,0,105,80,180,105,100,0,75,80,180]
stand_angles = [75, 90, 90, 105, 90, 90, 105, 90, 90, 75, 90, 90]
front_shoulders = [4, 0]
back_shoulders = [8,12]

sparky = SpotMicroStickFigure()

def set_servo_angle(s, a):
    active_servo = servo.Servo(pca.channels[servos[s][0]])
    active_servo.set_pulse_width_range(min_pulse=500, max_pulse=2500)
    active_servo.angle=a
    servos[s] = (servos[s][0], a)

def rest_position():
    for x in range(len(servos)):
        set_servo_angle(x, rest_angles[x])
    time.sleep(0.1)

def stand_straight():
    for x in range(len(servos)):
        set_servo_angle(x, stand_angles[x])
    time.sleep(0.1)

def roll_left(a):
    set_servo_angle(6, servos[6][1]+a)
    set_servo_angle(9, servos[9][1]+a)
    set_servo_angle(0, servos[0][1]-a)
    set_servo_angle(3, servos[3][1]-a)

def roll_right(a):
    set_servo_angle(6, servos[6][1]-a)
    set_servo_angle(9, servos[9][1]-a)
    set_servo_angle(0, servos[0][1]+a)
    set_servo_angle(3, servos[3][1]+a)

def set_body():
    sparky.set_body_angles(theta=10*pi/180)

if __name__=="__main__":
    stand_straight()
    while(True):
        action= input("What would you like to do?")
        if action=="sit":
            rest_position()
        elif action=="stand":
            stand_straight()
        elif action=="roll left":
            roll_left()
        elif action=="roll right":
            roll_right()
        else:
            break
        # time.sleep(5)
    # while(True):
    #     roll_left(10)
    #     time.sleep(2)
    #     roll_right(10)
    #     time.sleep(2)
    #     roll_right(10)
    #     time.sleep(2)
    #     roll_left(10)
    #     time.sleep(2)
    # try:
    #     set_body()
    #     while(True):
    #         rest_position()
    #         print(sparky.get_leg_angles())
    #         time.sleep(5)
    #         stand_straight()
    #         print(sparky.get_leg_angles())
    #         time.sleep(5)
    #         roll_left()
    #         time.sleep(5)
    # except:
    #     log.error("trouble connecting to the servos")
