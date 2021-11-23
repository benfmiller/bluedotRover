# from bluedot import BlueDot
# bd = BlueDot()
# bd.wait_for_press()
# print("You pressed the blue dot!")


# from bluedot import BlueDot
# from picamera import PiCamera
# from signal import pause

# bd = BlueDot()
# cam = PiCamera()

# def take_picture():
#     cam.capture("pic.jpg")

# bd.when_pressed = take_picture

# pause()


# from bluedot import BlueDot
# from gpiozero import Robot
# from signal import pause

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


from bluedot import BlueDot
from signal import pause

count = 0

def rotated(rotation):
    global count
    count += rotation.value

    print("{} {} {}".format(count,
                            rotation.clockwise,
                            rotation.anti_clockwise))

bd = BlueDot()
bd.when_rotated = rotated

pause()
