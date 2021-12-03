#!/usr/bin/env python3

from bluedot import BlueDot
from signal import pause
from gpiozero import Robot

lfpin = 4
lbpin = 14
rfpin = 17
rbpin = 18

bd = BlueDot()
robot = Robot(left=(lfpin, lbpin), right=(rfpin, rbpin))


def move(pos):
    if pos.top:
        robot.forward(pos.distance)
        print(f"robot forward: {pos.distance}")
    elif pos.bottom:
        robot.backward(pos.distance)
        print(f"robot backward: {pos.distance}")
    elif pos.left:
        robot.left(pos.distance)
        print(f"robot left: {pos.distance}")
    elif pos.right:
        robot.right(pos.distance)
        print(f"robot right: {pos.distance}")


def stop():
    robot.stop()


def bluedot_init():
    bd.when_pressed = move
    bd.when_moved = move
    bd.when_released = stop

    pause()


def main():
    bluedot_init()

if __name__ == "__main__":
    main()


# from bluedot import BlueDot
# from gpiozero import Robot
# from signal import pause

# lfpin = 4
# lbpin = 14
# rfpin = 17
# rbpin = 18

# bd = BlueDot()
# robot = Robot(left=(lfpin, lbpin), right=(rfpin, rbpin))


# def move(pos):
#     if pos.top:
#         robot.forward(pos.distance)
#     elif pos.bottom:
#         robot.backward(pos.distance)
#     elif pos.left:
#         robot.left(pos.distance)
#     elif pos.right:
#         robot.right(pos.distance)


# def stop():
#     robot.stop()


# bd.when_pressed = move
# bd.when_moved = move
# bd.when_released = stop

# pause()
