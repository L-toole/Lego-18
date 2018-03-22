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
    mpp.drive_condition(30, 30, onBlack, False)
    msleep(500)
    mpp.drive_condition(-30, -30, onBlack, True)
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
    if c.IS_BLUE_BOT:
        mpp.drive_timed(100, 79, 2.6)
    else: #IS_ORANGE_BOT
        mpp.drive_speed(16, 100)

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
    #Has failed multiple times
    #Need to use SENSORS
    if c.IS_BLUE_BOT:
        mpp.drive_timed(100, 77, 3.4)
    else: #IS_ORANGE_BOT
        #mpp.drive_speed(22, 100)
        #Please make this smoother
        x.lineFollowBounce(7.3, c.SIDE_TOPHAT)
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


def driveToCrates():
    print ("Driving to crates")
    if c.IS_ORANGE_BOT:
        pass
    else:
        mpp.drive_speed(-.5, 40)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawOpen)
    if c.IS_BLUE_BOT:
        mpp.drive_speed(1, 50)
        mpp.pivot_right(85,50)
    else: #IS_ORANGE_BOT
        mpp.pivot_right(88, 30)
        mpp.drive_till_black(60, 60)
    msleep(1000)
    if c.IS_BLUE_BOT:
        x.lineFollowRight(3.2)
    else: #IF_IS_ORANGE_BOT
        x.lineFollowRight(3)
        #u.waitForButton()
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
    if c.IS_BLUE_BOT:
        x.lineFollowLeft(5.5)
    else:
        x.lineFollowLeft(4)
    mpp.rotate(90, 30)
    mpp.drive_speed(9, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawOpen)
    # u.move_servo(c.servoClaw, c.clawFullyOpen)
    mpp.drive_speed(.5, 50)
    u.move_servo(c.servoArm, c.armDestack)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.drive_speed(-5, 30)
    msleep(500)
    mpp.rotate(-90, 30)
    if c.IS_BLUE_BOT:
        mpp.drive_speed(10, 50)
    else:
        mpp.drive_speed(12, 50)
    mpp.rotate(93, 30)
    msleep(200)
    mpp.drive_speed(3.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawFullyOpen)
    mpp.drive_speed(2, 50)
    mpp.drive_speed(-3, 50)
    mpp.drive_speed(4, 50)
    mpp.drive_speed(-6, 50)


def goYellowSecond():
    print('Going to yellow second position.')
    # Drive speed or sensor
    mpp.rotate(90, 20)
    x.lineFollowLeft(4)
    mpp.rotate(90, 30)
    #msleep(18000)
    mpp.drive_speed(7, 50) #changed here was 6
    mpp.pivot_right(95, 50)
    mpp.drive_speed(17, 70)
    mpp.rotate(-85, 50)
    mpp.drive_speed(-2.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel, 4)
    u.move_servo(c.servoClaw, c. clawFullyOpen)
    mpp.drive_speed(1, 50)
    u.move_servo(c.servoArm, c.armDestack)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.drive_speed(-5, 30)
    msleep(500)
    if c.IS_BLUE_BOT:
        mpp.rotate(-90, 30)
    else:
        mpp.rotate(-88, 30)
    mpp.drive_speed(12, 50)
    mpp.rotate(90, 30)
    msleep(200)
    if c.IS_BLUE_BOT:
        mpp.drive_speed(3.5, 50)
    else:
        mpp.drive_speed(3.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawFullyOpen)
    mpp.drive_speed(1, 50)
    mpp.drive_speed(-3, 50)
    mpp.drive_speed(4, 50)
    mpp.drive_speed(-6, 50)

    # Here you would use servos to drop the cube. However, that hardware does not currently exist.

def goYellowThird():
    print('Going to yellow third position.')
    mpp.rotate(-70, 50)
    x.lineFollowLeft(6)
    mpp.rotate(-90, 40)
    mpp.drive_till_black(60, 60)
    u.move_servo(c.servoArm, c.armBlockLevel, 4)
    u.move_servo(c.servoClaw, c. clawFullyOpen)
    mpp.drive_speed(1, 50)
    u.move_servo(c.servoArm, c.armDestack)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.drive_speed(-5, 30)
    msleep(500)
    if c.IS_BLUE_BOT:
        mpp.rotate(-90, 30)
    else:
        mpp.rotate(-88, 30)
    mpp.drive_speed(12, 50)
    mpp.rotate(90, 30)
    msleep(200)
    if c.IS_BLUE_BOT:
        mpp.drive_speed(3.5, 50)
    else:
        mpp.drive_speed(3.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawFullyOpen)
    mpp.drive_speed(1, 50)
    mpp.drive_speed(-3, 50)
    mpp.drive_speed(4, 50)
    mpp.drive_speed(-6, 50)

#Backs up to black line and turns
def goToBlackLineAndTurn():
    mpp.drive_till_black(-50, -50)
    mpp.drive_speed(-3, 60)
    u.move_servo(3, 1250, 10)
    mpp.rotate(100, 50)

#squares up on wall and black line
def squareUp():
    mpp.drive_speed(-18.5,50)
    mpp.drive_speed(2.8, 50)
    mpp.rotate(-82, 50)
    # mpp.drive_till_black(-50,50)
    # mpp.drive_timed(50,53, 1000)

def driveToYellow(): # Starts from the middle or it won't work and that's not our fault!
    p.determineOrder(colorOrder)
    if colorOrder[0] == c.YELLOW:
        goYellowFirst()
    elif colorOrder[1] == c.YELLOW:
        goYellowSecond()
    elif colorOrder[2] == c.YELLOW:
        goYellowThird()

def driveToFrisbees():
    print ("Driving to frisbees")
    mpp.drive_speed(-7, 60)

def onBlack():
    return analog(c.FRONT_TOPHAT) > c.TOPHAT_THRESHOLD


