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

def lineFollowBounce(time, port):
    sec = seconds()
    while (seconds() - sec < time):
        if(analog(port) > c.TOPHAT_THRESHOLD):
            drive(50, 100)
        elif(analog(port) < 500):
            drive(100,50)
        else:
            drive(100,100)
        drive(0, 0)