#!/usr/bin/python
from wallaby import *
import utils as u
import constants as c
import motorsPlusPlus as mpp


def driveTimed(left, right, time):
    motor(c.LMOTOR, left)
    motor(c.RMOTOR, right)
    msleep(time)
    ao()

def sleep(time):
    driveTimed(0, 0, time)

def drive(left, right):
    motor(c.LMOTOR,left)
    motor(c.RMOTOR,right)

def lineFollowLeft(time):
    sec = seconds()
    while(seconds()-sec<time):
        if(u.onBlackFront()):
            drive(45,60)#was 45
        else:
            drive(60,45) #was 45
    drive(0,0)

def lineFollowRight(time):
    sec = seconds()
    while(seconds()-sec<time):
        if(u.onBlackFront()):
            drive(60,45)
        else:
            drive(45,60)
    drive(0,0)


def lineFollowCondition(testFunction, state):
    print "lineFollowCondition"
    while testFunction() is state:
        if (u.onBlackFront()):
            drive(70, 100)
        else:
            drive(100, 70)
    drive(0, 0)

def rightOnBlack():
    return analog(c.RIGHT_TOPHAT) > c.TOPHAT_THRESHOLD