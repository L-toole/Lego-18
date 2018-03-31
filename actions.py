import drive as x
import utils as u
import constants as c
from wallaby import *
import motorsPlusPlus as mpp
import camera as p

colorOrder = []

def init():
    # starting positions
    # START WITH CLAW UP/OPEN!!!!!!!!!
    if c.IS_ORANGE_BOT:
        print("I AM ORANGE BOT!")
    elif c.IS_BLUE_BOT:
        print("I AM BLUE BOT!")
    else:
        print("I AM YELLOW BOT! !!!!!!!!!!")
        u.DEBUG()  # do not remove
    selfTest()
    p.cameraInit()
    msleep(100)
    u.waitForButton()
    c.startTime = seconds()

def selfTest():
    enable_servos()
    print ("Hola amigas")
    u.move_servo(c.servoArm, c.armMid)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmStartPosition)
    mpp.drive_condition(30, 30, leftOnBlack, False)
    msleep(500)
    mpp.drive_condition(-30, -30, onBlack, False)
    msleep(500)
    mpp.drive_condition(30, 30, rightOnBlack, False)
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
    mpp.drive_timed(-70, -70, 1)

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
        mpp.drive_speed(21,90)

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
    p.determineOrder(colorOrder)


def driveToCrates():
    print ("Driving to crates")
    #if c.IS_ORANGE_BOT:
    #    pass
    #else:
    #    mpp.drive_speed(-.5, 40)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawOpen)
    if c.IS_ORANGE_BOT:
        mpp.pivot_right(84, 30)
        mpp.drive_till_black(60, 60)
    else: #IS_BLUE_BOT
        mpp.pivot_right(80, 50)
        mpp.drive_till_black(60,60)
    #msleep(1000)
    if c.IS_ORANGE_BOT:
        x.lineFollowConditionSlow(backOnBlack, False)
        u.move_servo(c.servoClaw,c.clawOpen+100)
        mpp.drive_timed(50, 30, 0.8)
    else: #IS_BLUE_BOT
        x.lineFollowRight(2.8)#needs to be longer
    u.move_servo(c.servoClaw, c.clawClosed)
    msleep(600)
    u.move_servo(c.servoArm, c.armMid, 4)
    msleep(500)
    if c.IS_ORANGE_BOT:
        mpp.drive_condition(-90,-100, leftOnBlack, False)
    else:
        mpp.drive_speed(-7, 40)
    u.move_servo(c.servoArm, c.armHighMid, 4)

def driveToCenter():
    print ("Driving to center")
    mpp.drive_speed(4, 50)
    mpp.rotate(50, 40)
    mpp.drive_speed(24.5, 50)
    mpp.pivot_right(-15, 30)
    mpp.pivot_right(57, 30)
    mpp.drive_speed(11, 50)
    mpp.pivot_right(-90, 30)

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
    #line follow middle line to yellow
    x.lineFollowRight(10.4)
    mpp.rotate(-90, 30)
    mpp.drive_speed(3, 50)
    mpp.drive_condition(40, 40, onBlack, False)
    dropOffCrates()
    mpp.drive_speed(1, 50)
    mpp.drive_speed(-3, 50)
    mpp.drive_speed(4, 50)
    mpp.drive_speed(-6, 50)
    msleep(200)
    #drop off frisbee
    u.move_servo(c.servoArm, c.armUp)
    u.move_servo(c.servoClaw, c.clawClosed)
    mpp.pivot_right(-180, 30)
    #u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown, 5)
    mpp.rotate(90, 30)
    mpp.drive_speed(5, 50)
    u.DEBUG()

def goYellowThird():
    print('Going to yellow third position.')
    mpp.rotate(-70, 50)
    x.lineFollowRight(6)
    mpp.rotate(-90, 40)
    mpp.drive_condition(60,60,u.onBlackFront, False)
    dropOffFarCrate1()
    dropOffFarCrate2()

def dropOffCrates():
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawOpen)
    mpp.drive_speed(1.5, 50)  # .5
    u.move_servo(c.servoArm, c.armDestack)
    mpp.rotate(5, 10)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.rotate(-5, 10)
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

def dropOffFarCrate1():
    #mpp.drive_condition(-10, -10, onBlack, True)
    u.move_servo(c.servoArm, c.armBlockLevel)
    mpp.drive_speed(0.5,50)
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoArm, c.armDestack)
    #mpp.rotate(-2,10)
    u.move_servo(c.servoClaw, c.clawClosed,20)
    msleep(1000)
    u.move_servo(c.servoArm, c.armUp,20)
    msleep(3000)  # waiting for create
    print("waiting for create")

def dropOffFarCrate2():
    if c.IS_ORANGE_BOT:
        mpp.drive_condition(-100, -100, rightOnBlack, False)
        motor_power(c.LMOTOR, 100)
        msleep(1000)
        while not u.onBlackFront():
            pass
        ao()
        x.lineFollowLeft(1.8)
    else:
        # SHOULD BE LINE FOLLOW
        mpp.drive_speed(-6, 30)  # -5
        msleep(500)
        mpp.rotate(-88, 30)  # 90
        # mpp.drive_speed(10, 50)
    mpp.rotate(90, 30)  # 96
    msleep(200)
    mpp.drive_condition(50,50, u.onBlackFront, False)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawFullyOpen)
    mpp.drive_speed(1, 50)
    mpp.drive_speed(-3, 50)
    mpp.drive_speed(4, 50)
    mpp.drive_speed(-6, 50)


def driveToYellow(): # Starts from the middle or it won't work and that's not our fault!
    if colorOrder[0] == c.YELLOW:
        goYellowFirst()
        driveToFrisbees()
        dropOffFrisbee()
    elif colorOrder[1] == c.YELLOW:
        goYellowSecond()
    elif colorOrder[2] == c.YELLOW:
        goYellowThird()
        driveToFarFrisbees()
        u.DEBUG()
        dropOffFarFrisbee()

def driveToFrisbees():
    print ("Driving to frisbees")
    x.lineFollowCondition(leftOnBlack, False)
    mpp.drive_speed(4, 30) #was 1 inch
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
    mpp.drive_speed(-12, 60) #was 17 inches
    msleep(200)
    mpp.drive_speed(2.5, 60)
    mpp.rotate(-90, 30)
    mpp.drive_speed(-4, 50)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmPickUp)
    mpp.drive_speed(-2.5, 20)
    msleep(300)

def driveToFarFrisbees():
    print ("Driving to frisbees")
    u.move_servo(c.servoArm,c.armUp)
    mpp.pivot_right(-35,100)
    mpp.drive_condition(-75, -75,leftOnBlack, False)
    motor_power(c.RMOTOR, 100)
    msleep(500)
    motor_power(c.RMOTOR,75)
    while not u.onBlackFront():
        pass
    ao()
    mpp.drive_condition(100,100,rightOnBlack,False)
    motor_power(c.LMOTOR, 100)
    msleep(1000)
    while not u.onBlackFront():
        pass
    ao()
    mpp.drive_speed(-24,100)



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
    mpp.drive_speed(-5, 30) #was 8 inches
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown, 5)

def dropOffFarFrisbee():
    u.move_servo(c.servoArm, c.armUp)
    u.move_servo(c.servoClaw, c.clawClosed)

def onBlack():
    return analog(c.FRONT_TOPHAT) > c.TOPHAT_THRESHOLD

def leftOnBlack():
    return analog(c.LEFT_TOPHAT) > c.TOPHAT_THRESHOLD

def rightOnBlack():
    return analog(c.RIGHT_TOPHAT) > c.TOPHAT_THRESHOLD

def backOnBlack():
    return analog(c.BACK_TOPHAT) > c.TOPHAT_THRESHOLD

