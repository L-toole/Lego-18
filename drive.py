#!/usr/bin/python
from wallaby import *


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
        if(analog(0)<3600):
            drive(70,45)
        elif(analog(0)>3600 and analog(0)<100):
            drive(70,70)
        else:
            drive(45,70)
    drive(0,0)

def lineFollowRight(time):
    sec = seconds()
    while(seconds()-sec<time):
        if(analog(0)<1000):
            drive(55,60)
        elif(analog(0)>1000 and analog(0)<2000):
            drive(60,60)
        else:
            drive(60,55)
    drive(0,0)