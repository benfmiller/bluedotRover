#!/usr/bin/env python3

from bluedot import BlueDot
from signal import pause
from gpiozero import Robot
import RPi.GPIO as GPIO
import time

forwardpin = 17
backwardpin = 18
leftpin = 22
rightpin = 23

spreader_pin = 4

bd = BlueDot(cols=3)
# robot = Robot(left=(forwardpin, backwardpin), right=(leftpin, rightpin))
bd[1, 0].visible = False
bd[0, 0].square = True

GPIO.setmode(GPIO.BCM)

GPIO.setup(spreader_pin, GPIO.OUT)
pwm = GPIO.PWM(spreader_pin, 100)  # Initialize PWM on pwmPin 100Hz frequency

GPIO.setup(forwardpin, GPIO.OUT)
GPIO.setup(backwardpin, GPIO.OUT)
GPIO.setup(leftpin, GPIO.OUT)
GPIO.setup(rightpin, GPIO.OUT)

pwm_forward = GPIO.PWM(forwardpin, 100)  # Initialize PWM on pwmPin 100Hz frequency
pwm_backward = GPIO.PWM(backwardpin, 100)  # Initialize PWM on pwmPin 100Hz frequency
pwm_left = GPIO.PWM(leftpin, 100)  # Initialize PWM on pwmPin 100Hz frequency
pwm_right = GPIO.PWM(rightpin, 100)  # Initialize PWM on pwmPin 100Hz frequency

try:
    dc = 0  # set dc variable to 0 for 0%
    pwm.start(dc)  # Start PWM with 0% duty cycle
    pwm_forward.start(dc)
    pwm_backward.start(dc)
    pwm_left.start(dc)
    pwm_right.start(dc)

    def spreader(pos):
        vertical = (pos.y + 1) / 2
        percentage = round(vertical * 100, 2)
        print(f"{percentage}% vertical")
        if percentage < 40:
            pwm.ChangeDutyCycle(0)
        else:
            pwm.ChangeDutyCycle(percentage)

    def move(pos):
        # TODO refactor this
        if pos.x > 0:
            if pos.x > 0.2:
                pwm_right.ChangeDutyCycle(pos.x * 100)
                # robot.forward(pos.x)
            else:
                pwm_right.ChangeDutyCycle(0)
                # robot.forward(0)
        else:
            if pos.x < -0.2:
                pwm_left.ChangeDutyCycle(-1 * pos.x * 100)
                # robot.backward(-1 * pos.x)
            else:
                pwm_left.ChangeDutyCycle(0)
                # robot.forward(0)

        if pos.y > 0:
            if pos.y > 0.2:
                pwm_forward.ChangeDutyCycle(pos.y * 100)
                # robot.right(pos.y)
                # robot.right(1)
            else:
                pwm_forward.ChangeDutyCycle(0)
        else:
            if pos.y < -0.2:
                pwm_backward.ChangeDutyCycle(-1 * pos.y * 100)
                # robot.left(1)
                # robot.left(-1 * pos.y)
            else:
                pwm_backward.ChangeDutyCycle(0)
                # robot.left(0)

        print(f"robot x {pos.x}: robot y {pos.y}")

    def stop():
        # robot.stop()
        pwm_forward.ChangeDutyCycle(0)
        pwm_backward.ChangeDutyCycle(0)
        pwm_left.ChangeDutyCycle(0)
        pwm_right.ChangeDutyCycle(0)

    bd[0, 0].when_pressed = spreader
    bd[0, 0].when_moved = spreader

    bd[2, 0].when_pressed = move
    bd[2, 0].when_moved = move
    bd[2, 0].when_released = stop

    pause()

finally:
    pwm.stop()  # stop PWM
    pwm_forward.stop()
    pwm_backward.stop()
    pwm_left.stop()
    pwm_right.stop()
    GPIO.cleanup()  # resets GPIO ports used back to input mode
