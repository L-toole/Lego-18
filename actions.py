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
    if c.IS_ORANGE_BOT:
        print("I AM ORANGE BOT!")
    elif c.IS_BLUE_BOT:
        print("I AM BLUE BOT!")
    else:
        print("I AM YELLOW BOT!")
    selfTest()
    enable_servos()
    p.cameraInit()
    msleep(100)
    u.waitForButton()
    c.startTime = seconds()

def driveOutStartBox():
    #drives out of start box to pom
    if c.IS_BLUE_BOT:
        pass
    elif c.IS_YELLOW_BOT:
        mpp.drive_speed(18, 100)
    else: #IS_ORANGE_BOT
        mpp.drive_speed(19, 100)

def selfTest():
    u.move_servo(c.servoArm, c.armMid)
    msleep(750)
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    enable_servos()
    mpp.drive_condition(30, 30, onBlack, False)
    msleep(500)
    mpp.drive_condition(-30, -30, onBlack, True)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmUp)
    u.move_servo(c.servoFrisbeeGrabber, c.frisbeeGrabberOpen)
    u.move_servo(c.servoFrisbeeGrabber, c.frisbeeGrabberClosed)
    mpp.rotate(-20, 30)
    mpp.rotate(20, 30)


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

    if c.IS_BLUE_BOT:
        mpp.drive_speed(20,100)
    elif c.IS_YELLOW_BOT:
        mpp.drive_speed(25.5, 100)
    else: #IS_ORANGE_BOT
        mpp.drive_speed(22, 100)

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
    mpp.drive_speed(-.5, 40)
    if c.IS_BLUE_BOT:
        mpp.pivot_right(85,50)#92
    elif c.IS_YELLOW_BOT:
        mpp.pivot_right(85, 50)  # 92
    else: #IS_ORANGE_BOT
        mpp.pivot_right(87, 30) # 85
    msleep(1000)
    if c.IS_YELLOW_BOT:
        mpp.drive_speed(7, 100)
        u.move_servo(c.servoClaw, c.clawOpen)
        u.move_servo(c.servoArm, c.armBlockLevel)
        mpp.drive_speed(3.5, 50)
        mpp.rotate(-2, 20)
    elif c.IS_BLUE_BOT:
        mpp.drive_speed(9, 100)
        mpp.drive_speed(-2,-100)
        u.move_servo(c.servoClaw, c.clawOpen)
        u.move_servo(c.servoArm, c.armBlockLevel)
        mpp.drive_speed(2.5, 50)
    else: #IF_IS_ORANGE_BOT
        mpp.drive_speed(5, 100)
        u.move_servo(c.servoArm, c.armBlockLevel)
        u.move_servo(c.servoClaw, c.clawOpen)
        u.DEBUG()
        mpp.drive_speed(2.5, 50)
    u.move_servo(c.servoClaw, c.clawClosed)
    msleep(600)
    u.move_servo(c.servoArm, c.armMid, 4)
    msleep(500)
    if c.IS_YELLOW_BOT:
        mpp.rotate(2, 20)
        mpp.drive_speed(-4, 40)
    else:
        mpp.drive_speed(-5, 40)

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
    mpp.pivot_right(57, 50)
    mpp.drive_speed(11, 50)
    mpp.pivot_right(-90, 50)

def goYellowFirst():
    print('Going to yellow first position.')
    mpp.rotate(-100, 50)

def goYellowSecond():
    print('Going to yellow second position.')
    # Drive speed or sensor
    mpp.drive_speed(5, 70)
    mpp.drive_till_black(20, 20)
    #mpp.drive_speed(-1, 20)
    u.move_servo(c.servoClaw, c.clawOpen)
    # mpp.rotate(-10, 20)
    u.move_servo(c.servoArm, c.armDestack, 5)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.drive_speed(-2, 30)
    mpp.rotate(-40, 30)
    #Drive speed or sensor
    #mpp.drive_speed(.5, 40)
    mpp.drive_till_black(40,40)
    #next few lines attempt to fix the problem with the angle of the drop and its possible error
    mpp.drive_timed(20, 40, 3)
    mpp.drive_till_black(-40,-40)
    mpp.drive_speed(-3, 20)
    u.move_servo(c.servoArm, c.armBlockLevel, 5)
    # mpp.rotate(10, 30)
    #u.move_servo(c.servoClaw, c.clawOpen)
    #mpp.drive_speed(-5, 50)
    #mpp.rotate(180, 30)

    # Here you would use servos to drop the cube. However, that hardware does not currently exist.

def goYellowThird():
    print('Going to yellow third position.')
    mpp.rotate(15, 50)

def driveToYellow(): # Starts from the middle or it won't work and that's not our fault!
    p.determineOrder(colorOrder)
    if colorOrder[0] == c.YELLOW:
        goYellowFirst()
    elif colorOrder[1] == c.YELLOW:
        goYellowSecond()
    elif colorOrder[2] == c.YELLOW:
        goYellowThird()


def onBlack():
    return analog(c.FRONT_TOPHAT) > c.TOPHAT_THRESHOLD
