#!/usr/bin/python

import actions as act
import utils as u
import drive as d
import motorsPlusPlus as mpp

def main():
    print ("hello People")
    act.init()
    act.driveOutStartBox()
    act.sortPoms()
    act.turnAndDrive()
    act.sortSecondPile()
    act.driveToNextPoms()
    act.sortThirdPile()
    act.driveToDeposit()
    u.DEBUG()
    act.goToAquifer()
    u.DEBUG()

if __name__ == "__main__":
    main()