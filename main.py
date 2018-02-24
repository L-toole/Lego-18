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
    print ("Running")
    act.selfTest()
    act.init()
    act.driveOutStartBox()
    act.redOnTop()
    act.turnAndSort2()
    act.turnAndSort3()
    act.seeBlocks()
    u.DEBUG()
    act.greenOnTop()
    act.driveToNextPoms()
    act.redOnTop()
    act.driveToDeposit()
    act.goToAquifer()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
