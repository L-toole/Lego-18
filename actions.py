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
    u.wait_4_light()
    shut_down_in(119.5)
    c.startTime = seconds()

def selfTest():
    enable_servos()
    print ("Hola amigos")
    u.move_servo(c.servoArm, c.armMid)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmStartPosition)
    mpp.drive_condition(60, 60, leftOnBlack, False)
    msleep(500)
    mpp.drive_condition(-60, -60, onBlack, False)
    msleep(500)
    mpp.drive_condition(60, 60, backOnBlack, False)
    msleep(500)
    mpp.drive_condition(-60, -60, rightOnBlack, False)
    mpp.rotate(-20, 30)
    mpp.rotate(20, 30)
    msleep(750)
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoClaw, c.clawFullyOpen)
    u.move_servo(c.servoArm, c.armStartBoxPosition)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmStartPosition)
    mpp.drive_timed(-70, -70, 2)

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
    if colorOrder[0] == 3:
        u.move_servo(c.servoFrisbeeArm, c.frisbeeArmStartPosition+250)
        msleep(300)
        u.move_servo(c.servoFrisbeeArm, c.frisbeeArmStartPosition)


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
    if colorOrder[1] == 3:
        u.move_servo(c.servoFrisbeeArm, c.frisbeeArmStartPosition+250)
        msleep(300)
        u.move_servo(c.servoFrisbeeArm, c.frisbeeArmStartPosition)
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
        mpp.drive_speed(-1, 50)
    else:
        mpp.drive_speed(.5,50)
    mpp.pivot_right(84, 50)
    mpp.drive_till_black(60, 60)
    #Just added this to prevent turn off line in line follow
    mpp.drive_speed(2, 50)
    #msleep(1000)
    x.lineFollowConditionSlow(backOnBlack, False)
    u.move_servo(c.servoClaw,c.clawOpen+100)
    mpp.drive_timed(50, 30, 0.8)
    u.move_servo(c.servoClaw, c.clawClosed)
    msleep(600)
    u.move_servo(c.servoArm, c.armMid, 4)
    msleep(500)
    mpp.drive_condition(-90,-100, leftOnBlack, False)
        #mpp.drive_speed(-7, 40)
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
    mpp.rotate(90, 30)
    # Change these to use the corner black line
    # x.lineFollowCondition(leftOnBlack, False)
    if c.IS_ORANGE_BOT:
        x.lineFollowLeft(5.1)
    else:
        x.lineFollowLeft(4.3)
    #Do we need to change to a stop at corner black tape
    mpp.rotate(90, 30)
    mpp.drive_speed(9, 50)
    mpp.drive_condition(-10, -10, onBlack, True)
    dropOffCrates()
    mpp.drive_speed(2, 50)
    mpp.drive_speed(-3, 50)
    mpp.drive_speed(4, 50)
    #Different pattern
    if c.IS_ORANGE_BOT:
        mpp.drive_speed(-6, 50)
    else:
        mpp.drive_speed(-7, 50)
    mpp.arc_radius(90, 4.3, -60)
    mpp.drive_speed(-5, 60)


def goYellowSecond():
    #Maybe break this function up
    print('Going to yellow second position.')
    # Drive speed or sensor
    mpp.rotate(90, 30)
    driveToFrisbees()
    mpp.drive_speed(8, 50)
    mpp.drive_condition(60, 60, onBlack, False)
    mpp.drive_condition(60, 60, onBlack, True)
    mpp.drive_condition(60, 60, onBlack, False)
    mpp.drive_condition(60, 60, onBlack, True)
    if c.IS_ORANGE_BOT:
        mpp.drive_speed(1, 40)
    else:
        mpp.drive_speed(2, 45)
    mpp.rotate(90, 40)
    #line follow middle line to yellow
    x.lineFollowRight(3)
    msleep(2500)
    x.lineFollowConditionSlow(leftOnBlack, False)
    mpp.drive_speed(8.5, 60)
    mpp.rotate(-90, 40)
    mpp.drive_condition(50, 50, onBlack, False)
    fasterDropOffCrates()
    mpp.drive_speed(3.5, 60) #-1
    mpp.drive_speed(-.5, 60)
    mpp.drive_speed(1, 60)
    mpp.drive_speed(-5, 60)
    msleep(200)
    #drop off frisbee
    u.move_servo(c.servoArm, c.armUp, 25)
    u.move_servo(c.servoClaw, c.clawClosed, 25)
    mpp.rotate(-150, 50)
    mpp.drive_timed(60, 60, 2.5)
    msleep(10000)
    mpp.drive_timed(-60, -60, 2.5)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmHorizontal, 4)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown)
    u.DEBUG()

def goYellowThird():
    print('Going to yellow third position.')
    mpp.rotate(-70, 50)
    #Change these to use the corner black line
    #x.lineFollowCondition(leftOnBlack, False)
    if c.IS_ORANGE_BOT:
        x.lineFollowConditionSlow(rightOnBlack, False)
        mpp.drive_speed(-4, 40)
    else:
        x.lineFollowRight(6.3)
    mpp.rotate(-90, 40)
    mpp.drive_condition(-40, -40, rightOnBlack, False)
    mpp.drive_condition(-20, 1, leftOnBlack, False)
    mpp.rotate(-3, 30)
    mpp.drive_condition(60, 60, onBlack, False)
    msleep(9000)
    dropOffCrates()
    mpp.drive_speed(-1, 50)
    mpp.drive_speed(3, 50)
    mpp.drive_speed(-2, 50)
    mpp.drive_speed(2.5, 50)
    mpp.drive_speed(-2.5, 50)
    #dropOffFarCrate1()
    #dropOffFarCrate2()

def dropOffCrates():
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawOpen)
    mpp.drive_speed(1.5, 50)  # .5
    u.move_servo(c.servoArm, c.armDestack)
    mpp.rotate(1, 10)
    u.move_servo(c.servoClaw, c.clawClosed)
    u.move_servo(c.servoArm, c.armUp)
    mpp.rotate(-5, 10)
    mpp.drive_speed(-6, 30)  # -5
    msleep(500)
    mpp.rotate(-88, 30)  # 90
    mpp.drive_speed(10.5, 50)
    mpp.rotate(90, 30)  # 96
    msleep(200)
    #Initial value?
    mpp.drive_speed(3.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawFullyOpen)

def fasterDropOffCrates():
    u.move_servo(c.servoArm, c.armBlockLevel, 15)
    u.move_servo(c.servoClaw, c.clawOpen, 15)
    mpp.drive_speed(1.5, 70)
    u.move_servo(c.servoArm, c.armDestack, 15)
    mpp.rotate(1, 40)
    u.move_servo(c.servoClaw, c.clawClosed, 15)
    u.move_servo(c.servoArm, c.armUp, 15)
    mpp.rotate(-5, 40)
    mpp.drive_speed(-3, 60)
    mpp.rotate(-82, 40) #-86
    mpp.drive_speed(12, 50)
    mpp.rotate(90, 40)
    mpp.drive_speed(.5, 50)
    u.move_servo(c.servoArm, c.armBlockLevel)
    u.move_servo(c.servoClaw, c.clawFullyOpen)

#Why do we have new functions for drop off
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
        driveToFrisbeesFar()
        dropOffFrisbeeFar()

def driveToFrisbees():
    print ("Driving to frisbees")
    x.lineFollowCondition(leftOnBlack, False)
    mpp.drive_speed(4, 30) #was 1 inch
    msleep(200)
    mpp.rotate(90, 30)
    msleep(200)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmUp)
    mpp.drive_condition(-40, -40, leftOnBlack, False)
    mpp.drive_condition(1, -20, rightOnBlack, False)
    mpp.rotate(-3, 20)
    mpp.drive_speed(-20, 80)#-12
    msleep(200)
    mpp.drive_speed(6, 60)
    msleep(200)
    mpp.rotate(87, 30)
    msleep(200)
    mpp.drive_speed(-12, 60) #was 17 inches
    msleep(200)
    mpp.drive_speed(2.5, 60)
    mpp.rotate(-85, 30)
    msleep(500)
    mpp.drive_speed(-2.6, 30)
    mpp.drive_timed(-20, -10, .4)
    mpp.drive_timed(-10, -20, .4)
    mpp.drive_timed(-20, -10, .4)
    mpp.drive_timed(-10, -20, .4)
    mpp.drive_timed(-10, -10, .4)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmUp-100, 3) #May need to change position bc it is too high
    mpp.drive_timed(-10, -10, 1)
    msleep(200)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmPickUp, 4)
    mpp.drive_speed(-2.5, 20)
    msleep(300)

def driveToFrisbeesFar():
    print ("Driving to frisbees position 3")
    mpp.drive_condition(-70, -70, rightOnBlack, False)
    mpp.drive_condition(-20, 1, leftOnBlack, False)
    mpp.drive_speed(3.5, 70)
    mpp.rotate(90, 60)
    x.lineFollowConditionSlow(rightOnBlack, False)
    mpp.drive_speed(4, 70) #was 1 inch
    msleep(200)
    mpp.rotate(-90, 50)
    msleep(200)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmUp)
    mpp.drive_condition(-60, -60, rightOnBlack, False)
    mpp.drive_condition(-20, 1, leftOnBlack, False)
    mpp.rotate(-3, 40)
    mpp.drive_speed(-20, 80)#-12
    mpp.drive_speed(6, 60)
    mpp.rotate(-87, 30)
    mpp.drive_speed(-12, 60) #was 17 inches
    mpp.drive_speed(0.4, 60)
    mpp.rotate(85, 30)
    mpp.drive_speed(-2.6, 30)
    mpp.drive_timed(-30, -15, .2)
    mpp.drive_timed(-15, -30, .2)
    mpp.drive_timed(-30, -15, .2)
    mpp.drive_timed(-15, -30, .2)
    mpp.drive_timed(-20, -20, .2)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmUp-100, 3)
    mpp.drive_timed(-20, -20, .5)
    msleep(200)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmPickUp, 4)
    mpp.drive_speed(-2.5, 50)
    msleep(300)

# def driveToFarFrisbees():
#     print ("Driving to frisbees")
#     u.move_servo(c.servoArm,c.armUp)
#     mpp.pivot_right(-35,100)
#     mpp.drive_condition(-75, -75,leftOnBlack, False)
#     motor_power(c.RMOTOR, 100)
#     msleep(500)
#     motor_power(c.RMOTOR,75)
#     while not u.onBlackFront():
#         pass
#     ao()
#     mpp.drive_condition(60,60,rightOnBlack,False)
#     msleep(200)
#     motor_power(c.LMOTOR, 60)
#     msleep(1000)
#     while not u.onBlackFront():
#         pass
#     ao()
#     mpp.drive_speed(-24,70)


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
    if c.IS_ORANGE_BOT:
        mpp.drive_speed(-6.5, 30) #was 8 inches
    else:
        mpp.drive_speed(-5.5, 28)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmHorizontal, 4)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown)

def dropOffFrisbeeFar():
    u.move_servo(c.servoArm, c.armUp, 20)
    u.move_servo(c.servoClaw, c.clawClosed, 20)
    mpp.drive_speed(8, 70)
    mpp.drive_condition(70, 70, onBlack, False)
    mpp.drive_condition(70, 70, onBlack, True)
    mpp.drive_condition(70, 70, onBlack, False)
    mpp.drive_condition(70, 70, onBlack, True)
    mpp.rotate(-75, 50)
    x.lineFollowLeft(4.8)
    mpp.rotate(-90, 50)
    mpp.drive_condition(-50, -50, onBlack, False)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmHorizontal, 4)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmDown)
    u.DEBUG()

def dropOffFarFrisbee():
    u.move_servo(c.servoArm, c.armUp)
    u.move_servo(c.servoClaw, c.clawClosed)
    msleep(300)
    mpp.drive_speed(6, 70)
    msleep(200)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmUp)
    mpp.rotate(-90, 30)
    msleep(200)
    mpp.drive_speed(-12, 60)  # was 17 inches
    msleep(200)
    mpp.drive_speed(1.5, 60)
    mpp.rotate(90, 30)
    msleep(500)
    mpp.drive_speed(-4.3, 40)
    msleep(200)
    u.move_servo(c.servoFrisbeeArm, c.frisbeeArmPickUp, 5)
    mpp.drive_speed(-2.5, 20)


def onBlack():
    return analog(c.FRONT_TOPHAT) > c.TOPHAT_THRESHOLD

def leftOnBlack():
    return analog(c.LEFT_TOPHAT) > c.TOPHAT_THRESHOLD

def rightOnBlack():
    return analog(c.RIGHT_TOPHAT) > c.TOPHAT_THRESHOLD

def backOnBlack():
    return analog(c.BACK_TOPHAT) > c.TOPHAT_THRESHOLD

