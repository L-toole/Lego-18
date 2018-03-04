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
    if c.IS_PRIME:
        print("I AM PRIME")
    elif c.IS_CLONE_BLUE:
        print("I AM CLONE BLUE")
    else:
        print("I AM CLONE YELLOW")
    selfTest()
    enable_servos()
    p.cameraInit()
    set_servo_position(c.servoArm, c.armUp)
    msleep(100)
    u.waitForButton()
    c.startTime = seconds()

def driveOutStartBox():
    #drives out of start box to pom
    if c.IS_CLONE_BLUE:
        pass
    elif c.IS_CLONE_YELLOW:
        mpp.drive_speed(18, 100)
    else:
        mpp.drive_speed(22, 100)




#Code assumes that you are already lined up with the first block
#You may need to change the length of the line follow based on position
def seeBlocks():
    s = p.checkColor(colorOrder)
    if s == c.RED:
        print("found red")
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")
        u.DEBUG()

def driveToSecondBlock():

    if c.IS_CLONE_BLUE:
        mpp.drive_speed(20,100)
    elif c.IS_CLONE_YELLOW:
        mpp.drive_speed(25.5, 100)
    else:
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
    elif s == c.YELLOW:
        print("found yellow")
    elif s == c.GREEN:
        print("found green")
    else:
        print("Did not find cube")
        u.DEBUG()

def driveToCrates():
    mpp.pivot_right(92,50)
    mpp.drive_speed(9, 100)
    msleep(2000)
    if c.IS_CLONE_YELLOW:
        mpp.drive_speed(-2, 45)
    elif c.IS_CLONE_BLUE:
        mpp.drive_speed(-2,-100)
    else:
        mpp.drive_speed(-2, -100)
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoArm, c.armBlockLevel)
    mpp.drive_speed(2.5, 50)
    u.move_servo(c.servoClaw, c.clawClosed)
    msleep(600)
    u.move_servo(c.servoArm, c.armMid, 4)
    msleep(500)
    mpp.drive_speed(-4, 40)

def driveToFrisbees():
    mpp.rotate(-120, 30)
    mpp.drive_timed(-50,-50, 7)
    mpp.drive_timed(-50,-70, 2)
    mpp.pivot_right(-54, 50)
    mpp.drive_speed(-4, 50)
    msleep(2000)

def driveToCenter():
    mpp.drive_speed(4, 50)
    mpp.rotate(45, 40)
    mpp.drive_speed(24.5, 50)
    mpp.pivot_right(-15, 50)

def goYellowFirst():
    print('Going to yellow first position.')
# THIS COMMENTED OUT CODE SEEMS TO MAKE LEGO CHUCK THE CUBES OFF THE BOARD SO I AM STARTING FROM SCRATCH
# IF THIS CODE DOES SOMETHING IMPORTANT IT IS STILL HERE
#    mpp.drive_speed(6, 50)
#    mpp.rotate(-93, 50)
#    mpp.drive_speed(12, 50)
#    mpp.rotate(93, 50)
    mpp.rotate(-100, 50)

def goYellowSecond():
    print('Going to yellow second position.')
    mpp.drive_speed(7, 70)
    u.move_servo(c.servoClaw, c.clawOpen)
    # mpp.rotate(-10, 20)
    u.move_servo(c.servoArm, c.armDestack, 5)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.drive_speed(-2, 30)
    mpp.rotate(-40, 30)
    mpp.drive_speed(.5, 40)
    u.move_servo(c.servoArm, c.armBlockLevel, 5)
    # mpp.rotate(10, 30)
    #u.move_servo(c.servoClaw, c.clawOpen)
    #mpp.drive_speed(-5, 50)
    #mpp.rotate(180, 30)


    # Here you would use servos to drop the cube. However, that hardware does not currently exist.

def goYellowThird():
    print('Going to yellow third position.')

def driveToYellow(): # Starts from the middle or it won't work and that's not our fault!
    p.determineOrder(colorOrder)
    if colorOrder[0] == c.YELLOW:
        goYellowFirst()
    elif colorOrder[1] == c.YELLOW:
        goYellowSecond()
    elif colorOrder[2] == c.YELLOW:
        goYellowThird()

def selfTest():
    mpp.drive_speed(4,40)
    mpp.drive_speed(4,-40)
    mpp.rotate(-20,30)
    mpp.rotate(20,30)
    enable_servos()
    u.move_servo(c.servoArm, c.armMid)
    msleep(2000)
    u.move_servo(c.servoArm, c.armUp)
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoClaw, c.clawClosed)