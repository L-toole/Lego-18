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
        mpp.drive_speed(16, 70)
    elif c.IS_YELLOW_BOT:
        mpp.drive_speed(18, 100)
    else: #IS_ORANGE_BOT
        mpp.drive_speed(16, 100)


def selfTest():
    enable_servos()
    print ("Hola amigos")
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
        mpp.drive_speed(22, 100)
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
    #u.waitForButton()
    if c.IS_ORANGE_BOT:
        pass
    else:
        mpp.drive_speed(-.5, 40)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawOpen)
    if c.IS_BLUE_BOT:
        mpp.pivot_right(85,50)#92
    elif c.IS_YELLOW_BOT:
        mpp.pivot_right(85, 50)  # 92
    else: #IS_ORANGE_BOT
        mpp.pivot_right(78, 30)  #75
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
        # mpp.drive_speed(5, 100)
        #u.waitForButton()
        x.lineFollowRight(3.2)
    u.move_servo(c.servoClaw, c.clawClosed)
    msleep(600)
    u.move_servo(c.servoArm, c.armMid, 4)
    msleep(500)
    if c.IS_YELLOW_BOT:
        mpp.rotate(2, 20)
        mpp.drive_speed(-4, 40)
    elif c.IS_ORANGE_BOT:
        mpp.drive_speed(-8, 40)
    else:
        mpp.drive_speed(-5, 40)
    u.move_servo(c.servoArm, c.armHighMid, 4)

def driveToFrisbees():
    mpp.rotate(-120, 30)
    u.move_servo(c.servoFrisbeeGrabber, c.frisbeeGrabberOpen)
    u.move_servo(c.servoFrisbeeArm, c.armFrisbee)
    mpp.drive_timed(-50,-50, 6) #-50, -50, 7
    mpp.rotate(30, 30)
    mpp.drive_timed(-80, -80, 5.5)
    u.DEBUG()
    mpp.drive_timed(-50,-70, .5)
    mpp.pivot_right(-54, 50)
    mpp.drive_speed(2, 50)

def driveToCenter():
    u.DEBUG()
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
    x.lineFollowLeft(4)
    mpp.rotate(90, 30)
    mpp.drive_speed(9, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawOpen)
    # u.move_servo(c.servoClaw, c.clawFullyOpen)
    mpp.drive_speed(-1.5, 50)
    u.move_servo(c.servoArm, c.armDestack)
    mpp.drive_speed(1, 50)
    u.move_servo(c.servoClaw, c. clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.drive_speed(-4, 50)
    mpp.rotate(-38, 20)
    mpp.drive_speed(7.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel, 4)
    u.move_servo(c.servoClaw, c.clawFullyOpen)
    mpp.drive_speed(1.5, 50)
    u.move_servo(c.servoClaw, c.clawFullyOpen)
    msleep(300)
    mpp.drive_speed(-4, 50)



def goYellowSecond():
    print('Going to yellow second position.')
    # Drive speed or sensor
    mpp.rotate(180, 35)
    mpp.rotate(10, 50)
    mpp.drive_speed(9, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    # u.move_servo(c.servoClaw, c.clawFullyOpen)
    # mpp.drive_speed(1, 50)
    u.move_servo(c.servoArm, c.armDestack, 5)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp, 4)
    mpp.drive_speed(-4.5, 30)
    msleep(500)
    mpp.rotate(-100, 30)
    mpp.drive_speed(8, 50)
    mpp.rotate(90, 30)
    msleep(200)
    mpp.drive_speed(2.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawFullyOpen)
    mpp.drive_speed(1, 50)
    mpp.drive_speed(-6, 50)
    # mpp.drive_speed(8, 50)


    # Here you would use servos to drop the cube. However, that hardware does not currently exist.

def goYellowThird():
    print('Going to yellow third position.')
    mpp.rotate(-70, 50)
    x.lineFollowLeft(5)
    mpp.rotate(-90, 40)
    mpp.drive_speed(7, 50)
    mpp.rotate(13, 30)
    mpp.drive_speed(4.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel, 4)
    u.move_servo(c.servoClaw, c. clawFullyOpen)
    mpp.drive_speed(.5, 50)
    u.move_servo(c.servoArm, c.armDestack)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.drive_speed(-5, 30)
    msleep(500)
    mpp.rotate(-100, 30)
    mpp.drive_speed(8, 50)
    mpp.rotate(90, 30)
    msleep(200)
    mpp.drive_speed(2.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawFullyOpen)
    mpp.drive_speed(1, 50)
    mpp.drive_speed(-6, 50)


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
