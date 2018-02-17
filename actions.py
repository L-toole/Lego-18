import drive as x
import utils as u
import constants as c
from wallaby import *
import motorsPlusPlus as mpp


def init():
    #starting positions
    #START WITH CLAW UP/OPEN!!!!!!!!!
    enable_servos()
    set_servo_position(c.servoClaw, c.clawOpen)
    msleep(100)

def driveOutStartBox():
    #drives out of start box to pom
    mpp.drive_speed(7, 60)   #9.4


def redOnTop():
    u.move_servo(c.servoClaw, c.clawMiddle)
    u.move_servo(c.servoClaw, c.clawRedHalfOpen)

def turnAndDrive():
    x.driveTimed(30, 30, 1800)#4.4, 40  #60, 60, 1500
    u.move_servo(c.servoClaw, c.clawOpen, 20)
    mpp.pivot_right(-77, 40)
    u.move_servo(c.servoClaw, c.clawGreenHalfOpen, 20)
    mpp.drive_speed(5.3, 50)
    u.move_servo(c.servoClaw, c.clawMiddle)
    mpp.drive_speed(3, 50)
    mpp.pivot_left(33, 40)
    u.move_servo(c.servoClaw, c.clawOpen, 20)
    u.move_servo(c.servoClaw, c.clawCrossed, 20)
    u.move_servo(c.servoClaw, c.clawMiddle, 20)
    mpp.drive_speed(4, 50)
    mpp.drive_speed(4, 60)
    u.move_servo(c.servoClaw, c.clawRedHalfOpen)
    u.move_servo(c.servoClaw, c.clawStacked)
    mpp.drive_speed(3, 60)
    u.DEBUG()

def greenOnTop():
    #sorts pom pile with green on top
    u.move_servo(c.servoClaw, c.clawHalfOpen)
    msleep(100)
    '''u.move_servo(c.servoClaw, c.clawCrossed, 20)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen, 20)
    msleep(1000)
    u.move_servo(c.servoClaw, c.clawMiddle, 20)
    msleep(100)'''

def driveToNextPoms():
    mpp.drive_timed(70, 70, 2)
    mpp.drive_timed(90, 18, 1)
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