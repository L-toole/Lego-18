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
    print ("Running the code")
    #mpp.drive_speed(36,100)
    #msleep(500)
    #u.DEBUG()
    act.init()
    act.driveOutStartBox()
    act.seeBlocks()
    act.driveToSecondBlock()
    act.seeBlocksTwo()
    act.driveToCrates()
    act.driveToYellow()
    u.DEBUG()
    # act.driveToCenter()
    # act.driveToYellow()





if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
