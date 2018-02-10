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
    mpp.drive_speed(9.5, 70)

def sortPoms():
    #moves arm down
    #closes claw
    u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(1000)
    u.move_servo(c.servoClaw, c.clawMiddle)

def turnAndDrive():
    #drives forward to be centered on black line
    mpp.drive_speed(22, 40)#4.4, 40
    u.move_servo(c.servoClaw, c.clawOpen)
    mpp.drive_timed(-17,-100,1.85)
    u.move_servo(c.servoClaw, c.clawCrossed)

    #mpp.pivot_right(-7, 40)#127 degrees
    #mpp.drive_speed(5.5, 40)#was 4.5
    x.lineFollowLeft(1.2)
    ao() #alloff
    msleep(2000)

def sortSecondPile():
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawMiddle)
    msleep(100)
    mpp.drive_speed(3.75, 40)
    '''u.move_servo(c.servoClaw, c.clawCrossed)
    msleep(100)
    u.move_servo(c.servoClaw, c.clawOpen)
    msleep(1000)
    u.move_servo(c.servoClaw, c.clawMiddle)
    msleep(100)'''

def driveToNextPoms():
    x.lineFollowLeft(1.75) #mpp.drive_speed(7, 40)
    u.move_servo(c.servoClaw, c.clawOpen)
    x.lineFollowLeft(1)
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
    u.move_servo(c.servoClaw, c.clawMiddle)

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