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
        print("I AM YELLOW BOT! !!!!!!!!!!")
        u.DEBUG()  # do not remove
    selfTest()
    enable_servos()
    p.cameraInit()
    msleep(100)
    u.waitForButton()
    c.startTime = seconds()

def selfTest():
    enable_servos()
    print ("Hola amigas")
    u.move_servo(c.servoArm, c.armMid)
    mpp.drive_condition(30, 30, leftOnBlack, False)
    msleep(500)
    mpp.drive_condition(-30, -30, onBlack, False)
    mpp.rotate(-20, 30)
    mpp.rotate(20, 30)
    msleep(750)
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armStartBoxPosition)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmStartPosition)

def driveOutStartBox():
    #drives out of start box to pom
    if c.IS_ORANGE_BOT:
        # mpp.drive_timed(85, 105, 2.7)
        mpp.drive_speed(16, 90)
    else: #IS_BLUE_BOT
        # mpp.drive_timed(100, 79, 2.6)  # original
        mpp.drive_speed(16, 90)  # test

#Code assumes that you are already lined up with the first block
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


def driveToSecondBlock():
    if c.IS_ORANGE_BOT:
        # mpp.drive_speed(22, 100)
        mpp.drive_speed(22.5, 90)
    else: #IS_BLUE_BOT
        mpp.drive_timed(100, 77, 3.4)

# Code assumes that you are already lined up with the middle block
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

def driveToCrates():
    print ("Driving to crates")
    if c.IS_ORANGE_BOT:
        pass
    else:
        mpp.drive_speed(-.5, 40)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawOpen)
    if c.IS_ORANGE_BOT:
        mpp.pivot_right(84, 30)
        mpp.drive_till_black(60, 60)
    else: #IS_BLUE_BOT
        mpp.drive_speed(1, 50)
        mpp.pivot_right(85, 50)
    msleep(1000)
    if c.IS_ORANGE_BOT:
        x.lineFollowRight(3)
    else: #IS_BLUE_BOT
        x.lineFollowRight(3.2)
    u.move_servo(c.servoClaw, c.clawClosed)
    msleep(600)
    u.move_servo(c.servoArm, c.armMid, 4)
    msleep(500)
    if c.IS_ORANGE_BOT:
        mpp.drive_speed(-6.5, 40)
    else:
        mpp.drive_speed(-5, 40)
    u.move_servo(c.servoArm, c.armHighMid, 4)

def driveToCenter():
    print ("Driving to center")
    mpp.drive_speed(4, 50)
    mpp.rotate(50, 40)
    mpp.drive_speed(24.5, 50)
    mpp.pivot_right(-15, 50)
    mpp.pivot_right(57, 50)
    mpp.drive_speed(11, 50)
    mpp.pivot_right(-90, 50)

def goYellowFirst():
    print('Going to yellow first position.')
    mpp.rotate(90, 20)
    if c.IS_ORANGE_BOT:
        x.lineFollowLeft(4.3)#5
    else: #IS_BLUE_BOT
        x.lineFollowLeft(5.5)
    mpp.rotate(90, 30)
    mpp.drive_speed(9, 50)
    mpp.drive_condition(-10, -10, onBlack, True)
    dropOffCrates()
    mpp.drive_speed(2, 50)
    mpp.drive_speed(-3, 50)
    mpp.drive_speed(4, 50)
    #Different pattern
    mpp.drive_speed(-7, 50)
    mpp.arc_radius(90, 4.3, -60)
    mpp.drive_speed(-5, 60)


def goYellowSecond():
    #Maybe break this function up
    print('Going to yellow second position.')
    # Drive speed or sensor
    mpp.rotate(90, 10)
    driveToFrisbees()
    mpp.drive_speed(8, 50)
    mpp.drive_condition(50, 50, onBlack, False)
    mpp.drive_condition(50, 50, onBlack, True)
    mpp.drive_condition(50, 50, onBlack, False)
    mpp.drive_condition(50, 50, onBlack, True)
    mpp.rotate(90, 30)
    x.lineFollowRight(10.5)
    mpp.rotate(-90, 30)
    mpp.drive_speed(3, 50)
    mpp.drive_condition(40, 40, onBlack, False)
    dropOffCrates()
    mpp.drive_speed(1, 50)
    mpp.drive_speed(-3, 50)
    mpp.drive_speed(4, 50)
    mpp.drive_speed(-6, 50)
    msleep(200)
    u.move_servo(c.servoArm, c.armUp)
    u.move_servo(c.servoClaw, c.clawClosed)
    mpp.pivot_right(-180, 30)
    mpp.drive_speed(2, 40)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown, 5)

def goYellowThird():
    print('Going to yellow third position.')
    mpp.rotate(-70, 50)
    x.lineFollowLeft(6)
    mpp.rotate(-90, 40)
    mpp.drive_condition(60,60,u.onBlackFront, False)
    dropOffCrates()
    mpp.drive_speed(1, 50)
    mpp.drive_speed(-3, 50)
    mpp.drive_speed(4, 50)
    mpp.drive_speed(-6, 50)
    mpp.drive_speed(-6, 60)
    mpp.rotate(-90, 60)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown, 5)


def dropOffCrates():
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawOpen)
    mpp.drive_speed(1.5, 50)  # .5
    u.move_servo(c.servoArm, c.armDestack)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.drive_speed(-6, 30)  # -5
    msleep(500)
    mpp.rotate(-88, 30)  # 90
    if c.IS_ORANGE_BOT:
        mpp.drive_speed(12, 50)
    else:
        mpp.drive_speed(10, 50)
    mpp.rotate(90, 30)  # 96
    msleep(200)
    mpp.drive_speed(3.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawFullyOpen)

def driveToYellow(): # Starts from the middle or it won't work and that's not our fault!
    p.determineOrder(colorOrder)
    if colorOrder[0] == c.YELLOW:
        goYellowFirst()
        #Need these because the pattern for Yellow 2 is different
        driveToFrisbees()
        dropOffFrisbee()
    elif colorOrder[1] == c.YELLOW:
        goYellowSecond()
    elif colorOrder[2] == c.YELLOW:
        goYellowThird()
        driveToFrisbees()
        dropOffFrisbee()

def driveToFrisbees():
    print ("Driving to frisbees")
    x.lineFollowCondition(leftOnBlack, False)
    mpp.drive_speed(1, 30)
    msleep(200)
    mpp.rotate(90, 30)
    msleep(200)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmUp)
    mpp.drive_speed(-20, 80)#-12
    msleep(200)
    mpp.drive_speed(6, 60)
    msleep(200)
    mpp.rotate(90, 30)
    msleep(200)
    mpp.drive_speed(-17, 60)
    msleep(200)
    mpp.drive_speed(2.5, 60)
    mpp.rotate(-90, 30)
    mpp.drive_speed(-4, 50)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmPickUp)
    mpp.drive_speed(-2.5, 20)
    msleep(300)

def dropOffFrisbee():
    u.move_servo(c.servoArm, c.armUp)
    u.move_servo(c.servoClaw, c.clawClosed)
    mpp.drive_speed(8, 50)
    mpp.drive_condition(50, 50, onBlack, False)
    mpp.drive_condition(50, 50, onBlack, True)
    mpp.drive_condition(50, 50, onBlack, False)
    mpp.drive_condition(50, 50, onBlack, True)
    mpp.rotate(90, 30)
    x.lineFollowLeft(3.7)
    mpp.rotate(90, 30)
    mpp.drive_speed(-8, 30)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown, 5)


def onBlack():
    return analog(c.FRONT_TOPHAT) > c.TOPHAT_THRESHOLD

def leftOnBlack():
    return analog(c.LEFT_TOPHAT) > c.TOPHAT_THRESHOLD
