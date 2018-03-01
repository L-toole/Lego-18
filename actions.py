import drive as x
import utils as u
import constants as c
from wallaby import *
import motorsPlusPlus as mpp
import camera as p

colorOrder = []

def init():
    #starting positions
    #START WITH CLAW UP/OPEN!!!!!!!!!
    if c.IS_CLONE:
        print("I AM CLONE")
    elif c.IS_PRIME:
        print("I AM PRIME")
    else:
        print("I DON'T KNOW WHAT I AM")
    selfTest()
    #enable_servos()
    p.cameraInit()
    set_servo_position(c.servoClaw, c.clawOpen)
    msleep(100)
    u.waitForButton()

def driveOutStartBox():
    #drives out of start box to pom
    if c.IS_PRIME:
        mpp.drive_speed(21, 100)
    else:
        pass



#Code assumes that you are already lined up with the first block
#You may need to change the length of the line follow based on position
def seeBlocks():
    s = p.checkColor(colorOrder)
    if s == c.RED:
        print("found red")
    if s == c.YELLOW:
        print("found yellow")
    if s == c.GREEN:
        print("found green")

def driveToSecondBlock():
    mpp.drive_speed(20,100)

    # do something here
    # p.checkColor(colorOrder)
    # p.determineOrder(colorOrder)

    # Code assumes that you are already lined up with the middle block
    # You may need to change the length of the line follow based on position
def seeBlocksTwo():
    s = p.checkColor(colorOrder)
    if s == c.RED:
        print("found red")
    if s == c.YELLOW:
        print("found yellow")
    if s == c.GREEN:
        print("found green")

def driveToCrates():
    mpp.pivot_right(92,50)
    mpp.drive_speed(11,100)
    msleep(2000)
    mpp.drive_speed(2,-100)

def driveToFrisbees():
    mpp.rotate(-120, 50)
    mpp.drive_timed(-70,-70, 4)
    mpp.drive_timed(-50,-70, 2)
    mpp.pivot_right(-54, 50)
    mpp.drive_speed(-3, 50)
    msleep(500)

def driveToCenter():
    mpp.drive_speed(4, 50)
    mpp.pivot_left(-86, 50)
    mpp.drive_timed(80, 40, 2.5)
    mpp.drive_speed(24.5, 50)
    mpp.pivot_right(-43, 50)

def selfTest():
    mpp.drive_speed(4,40)
    mpp.drive_speed(4,-40)
    mpp.rotate(-20,30)
    mpp.rotate(20,30)
    enable_servos()
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoClaw, c.clawCrossed)
