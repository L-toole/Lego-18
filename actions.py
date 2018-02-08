import drive as x
import utils as u
import constants as c
from wallaby import *
import motorsPlusPlus as mpp


def init():
    #starting positions
    #START WITH CLAW UP!!!!!!!!!
    enable_servos()
    set_servo_position(c.servoClaw, c.clawOpen)
    msleep(100)

def driveOutStartBox():
    #drives out of start box to pom
    mpp.drive_speed(12.75, 70)

def sortPoms():
    #moves arm down
    #closes claw
    u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(1000)

def turnAndDrive():
    #drives forward to be centered on black line
    mpp.drive_speed(15, 40)#4.4, 40
    mpp.pivot_right(-128, 40)#127 degrees
    mpp.drive_speed(4, 40)#was 4.5
    ao() #alloff
    msleep(2000)

def sortSecondPile():
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(1000)

def driveToNextPoms():
    u.move_servo(c.servoClaw, c.clawMiddle)
    x.lineFollowLeft(2) #mpp.drive_speed(7, 40)
    u.move_servo(c.servoClaw, c.clawOpen)
    x.lineFollowLeft(1)#mpp.drive_speed(9.5, 40)
    '''
    while not u.onBlackFront():
        mpp._drive(75,50)
        print("on black")'''
    # x.lineFollowLeft(2.05)

def sortThirdPile():
    u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(1000)

def driveToDeposit():
    mpp.rotate(90, 40)
    mpp.drive_speed(14, 40)
    mpp.rotate(90, 40)
    x.lineFollowLeft(13)

def goToAquifer():
    mpp.rotate(90, 40)
    #Change this to a drive condition later
    while(analog(0)<1000):
        mpp._drive(60, 60)
    mpp.pivot_left(90, 40)
    x.lineFollowRight(2.5)