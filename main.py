#!/usr/bin/python
import os, sys
from wallaby import *
import actions as act
import utils as u
import constants as c
import drive as x
import drive as d
import motorsPlusPlus as mpp

def main():
    print ("hello Meeples")
    act.init()
    act.driveOutStartBox()
    act.redOnTop()
    act.turnAndDrive()
    act.greenOnTop()
    act.driveToNextPoms()
    act.redOnTop()
    act.driveToDeposit()
    act.goToAquifer()
    u.DEBUG()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
