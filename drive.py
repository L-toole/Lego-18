#!/usr/bin/python
from wallaby import *
import utils as u


def driveTimed(left, right, time):
    motor(0, left)
    motor(3, right)
    msleep(time)
    ao()

def sleep(time):
    driveTimed(0, 0, time)

def drive(left, right):
    motor(0,left)
    motor(3,right)

def lineFollowLeft(time):
    sec = seconds()
    while(seconds()-sec<time):
        if(u.onBlackFront()):
            drive(40,70)#was 45
        else:
            drive(70,40)#was 45
    drive(0,0)

def lineFollowRight(time):
    sec = seconds()
    while(seconds()-sec<time):
        if(u.onBlackFront()):
            drive(60,55)
        else:
            drive(55,60)
    drive(0,0)