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
    enable_servos()
    p.cameraInit()
    set_servo_position(c.servoClaw, c.clawOpen)
    msleep(100)
    u.waitForButton()

def driveOutStartBox():
    #drives out of start box to pom
    mpp.drive_speed(7, 60)   #9.4

def redOnTop():
    u.move_servo(c.servoClaw, c.clawMiddle)
    u.move_servo(c.servoClaw, c.clawRedHalfOpen)

def greenOnTop():
    # sorts pom pile with green on top
    u.move_servo(c.servoClaw, c.clawGreenHalfOpen)
    msleep(100)
    '''u.move_servo(c.servoClaw, c.clawCrossed, 20)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen, 20)
    msleep(1000)
    u.move_servo(c.servoClaw, c.clawMiddle, 20)
    msleep(100)'''

def turnAndSort2():
    x.driveTimed(40, 40, 1800)#4.4, 40  #60, 60, 1500
    u.move_servo(c.servoClaw, c.clawOpen, 20)
    mpp.pivot_right(-87, 40) #-80, 40
    u.move_servo(c.servoClaw, c.clawGreenHalfOpen, 20)
    mpp.drive_speed(5.3, 50)
    u.move_servo(c.servoClaw, c.clawMiddle)
    mpp.drive_speed(3, 50)
    mpp.pivot_left(30, 40)
    u.move_servo(c.servoClaw, c.clawOpen, 20)
    u.move_servo(c.servoClaw, c.clawCrossed, 20)
    u.move_servo(c.servoClaw, c.clawMiddle, 20)

def turnAndSort3():
    u.move_servo(c.servoClaw, c.clawAlmostOpen)
    mpp.drive_speed(9, 55)
    u.move_servo(c.servoClaw, c.clawGreenHalfOpen)
    u.move_servo(c.servoClaw, c.clawMiddle)
    u.move_servo(c.servoClaw, c.clawStacked)
    mpp.drive_speed(6, 60)
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoClaw, c.clawCrossed)
    x.driveTimed(18, 0, 1000)


#Code assumes that you are already lined up with the first block
#You may need to change the length of the line follow based on position
def seeBlocks():
    s = p.checkColor(colorOrder)
    if s == c.RED:
        dropRedNear()
    if s == c.YELLOW:
        seeYellow()
    if s == c.GREEN:
        dropGreenNearAndBackUp()


    # do something here
    # p.checkColor(colorOrder)
    # p.determineOrder(colorOrder)



def driveToNextPoms():
    mpp.drive_timed(70, 70, 2)
    mpp.drive_timed(90, 15, 1.1) #1
    msleep(300)
    u.move_servo(c.servoClaw, c.clawHalfOpen)
    '''x.lineFollowLeft(1.75) #mpp.drive_speed(7, 40)
    u.move_servo(c.servoClaw, c.clawOpen)
    x.lineFollowLeft(1)
    while not u.onBlackFront():
        mpp._drive(75,50)
        print("on black")'''
    # x.lineFollowLeft(2.05)

def driveToDeposit():
    x.lineFollowLeft(2.5)
    u.move_servo(c.servoClaw, c.clawOpen)
    x.lineFollowLeft(2)
    mpp.rotate(-125, 60)
    mpp.drive_speed(10, 40)

def goToAquifer():
    mpp.rotate(90, 40)
    #Change this to a drive condition later
    while(analog(0)<1000):
        mpp._drive(60, 60)
    mpp.pivot_left(90, 40)
    x.lineFollowRight(2.5)


def dropRedNear():
    print("Found Red...")
    u.move_servo(c.servoClaw, c.clawOpen)
    mpp.pivot_left(80, 30) #75
    u.move_servo(c.servoClaw, c.clawCrossed)
    mpp.drive_speed(10.7, 60) #10,60
    #mpp.rotate(-10, 30) #20,50
    mpp.drive_speed(8,-40)
    mpp.rotate(25, -40)
    mpp.drive_speed(4, 40)
    mpp.rotate(10,-30)
    mpp.drive_speed(2, 30)
    mpp.drive_speed(9, -40)
    mpp.drive_till_black(-30,-30 )
    mpp.rotate(115, 30)


def dropGreenNearAndBackUp():
    print("Found Green...")
    u.move_servo(c.servoClaw, c.clawOpen)
    mpp.pivot_left(123, 50)
    mpp.drive_speed(7.5, 60)   #8
    mpp.rotate(-10, 30)  #-10, 30
    mpp.drive_speed(1, 60)
    mpp.drive_speed(12, -60)
    u.move_servo(c.servoClaw, c.clawCrossed)
    #mpp.rotate(27, 50)
    mpp.drive_speed(8, 60)
    mpp.drive_till_black(30,30)
    print("Backing up")
    msleep(2000)
    mpp.drive_speed(-5.5, 40)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(500)
    mpp.drive_speed(-7, 60)
    mpp.drive_till_black(-30, -30)



def backOutbox():
    print("Backing up")
    msleep(2000)
    mpp.drive_speed(-5, 40)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(500)
    mpp.drive_speed(-7, 60)
    mpp.drive_till_black(-30, -30)



def seeYellow():
    mpp.drive_speed(24,50)
    s = p.checkColor(colorOrder)
    if s == c.RED:
        dropRedNear()
    if s == c.YELLOW:
        print("Found yellow...")
        mpp.pivot_left(50, 50)
    if s == c.GREEN:
        dropGreenNear()

def selfTest():
    mpp.drive_speed(4,40)
    mpp.drive_speed(4,-40)
    mpp.rotate(20,30)
    mpp.rotate(-20,30)
    enable_servos()
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoClaw, c.clawCrossed)
