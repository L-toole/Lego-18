#!/usr/bin/python
from wallaby import *
import actions as act
import utils as u
import constants as c
import drive as x
import drive as d
import motorsPlusPlus as mpp

def main():
    print ("hello People")
    act.init()
    act.driveOutStartBox()
    act.redOnTop()
    act.turnAndDrive()
    act.greenOnTop()
    act.driveToNextPoms()
    u.DEBUG()
    act.redOnTop()
    u.DEBUG()
    act.driveToDeposit()
    act.goToAquifer()
    u.DEBUG()

if __name__ == "__main__":
    main()