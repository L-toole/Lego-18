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
    #sorts pom pile with red on top
    #moves arm down
    #closes claw
    u.move_servo(c.servoClaw, c.clawMiddle)
    u.move_servo(c.servoClaw, c.clawRedHalfOpen)

def turnAndDrive():
    #drives forward to be centered on black line
    x.driveTimed(30, 30, 1800)#4.4, 40  #60, 60, 1500
    u.move_servo(c.servoClaw, c.clawOpen)
    mpp.pivot_right(-77, 40)
    u.move_servo(c.servoClaw, c.clawGreenHalfOpen)
    mpp.drive_speed(5.3, 50)
    u.move_servo(c.servoClaw, c.clawMiddle)
    mpp.drive_speed(3, 50)
    mpp.pivot_left(48, 40)
    u.move_servo(c.servoClaw, c.clawOpen)
    u.move_servo(c.servoClaw, c.clawCrossed)
    u.move_servo(c.servoClaw, c.clawMiddle)
    mpp.drive_speed(4, 50)
    u.DEBUG()
    mpp.drive_speed(9, 65)
    u.DEBUG()
    #mpp.pivot_right(-7, 40)#127 degrees
    #mpp.drive_speed(5.5, 40)#was 4.5
    #x.lineFollowLeft(1.2)
    #ao() #alloff
    #msleep(2000)

def greenOnTop():
    #sorts pom pile with green on top
    u.move_servo(c.servoClaw, c.clawHalfOpen)
    msleep(100)
    '''u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(1000)
    u.move_servo(c.servoClaw, c.clawMiddle)
    msleep(100)'''

def driveToNextPoms():
    u.move_servo(c.servoClaw, c.clawHalfCrossed)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawHalfOpen)
    x.driveTimed(70, 70, 2000)
    u.move_servo(c.servoClaw,c.clawOpen)
    mpp.drive_timed(90, 18, 1.5)
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