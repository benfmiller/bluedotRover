#!/usr/bin/env python3

from bluedot import BlueDot
from signal import pause
from gpiozero import Robot
import RPi.GPIO as GPIO
import time


def spreader(pos):
    vertical = (pos.y + 1) / 2
    percentage = round(vertical * 100, 2)
    print(f"{percentage}% vertical")
    # pwm.ChangeDutyCycle(percentage)


def move(pos):
    # TODO refactor this
    if pos.y > 0:
        robot.forward(pos.y)
    else:
        robot.backward(-1 * pos.y)

    if pos.x > 0:
        robot.right(pos.x)
    else:
        robot.left(-1 * pos.x)

    print(f"robot x {pos.x}: robot y {pos.y}")


def stop():
    robot.stop()


lfpin = 17
lbpin = 18
rfpin = 22
rbpin = 23

spreader_pin = 4

bd = BlueDot(cols=3)
robot = Robot(left=(lfpin, lbpin), right=(rfpin, rbpin))
bd[1, 0].visible = False
bd[0, 0].square = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(spreader_pin, GPIO.OUT)
pwm = GPIO.PWM(spreader_pin, 100)  # Initialize PWM on pwmPin 100Hz frequency
dc = 0  # set dc variable to 0 for 0%
pwm.start(dc)  # Start PWM with 0% duty cycle

bd[0, 0].when_pressed = spreader
bd[0, 0].when_moved = spreader

bd[2, 0].when_pressed = move
bd[2, 0].when_moved = move
bd[2, 0].when_released = stop

pause()

pwm.stop()  # stop PWM
GPIO.cleanup()  # resets GPIO ports used back to input mode
