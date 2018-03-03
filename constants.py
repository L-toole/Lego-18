import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 3
RMOTOR = 0

# Digital ports
CLONE_SWITCH_YELLOW = 0
CLONE_SWITCH_BLUE = 1

RIGHT_BUTTON = 13

IS_CLONE_YELLOW = w.digital(CLONE_SWITCH_YELLOW)
IS_CLONE_BLUE = w.digital(CLONE_SWITCH_BLUE)
IS_PRIME = not IS_CLONE_YELLOW and not IS_CLONE_BLUE


if IS_PRIME:
    # Servos
    servoClaw = 0

    #camera channels
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

    #color tolerances
    COLOR_PROXIMITY=20
    ORANGE_AREA=500
    RGY_AREA=100

    #Claw position values
    clawOpen = 0
    clawAlmostOpen= 500
    clawHalfCrossed = 640
    clawMiddle = 650
    clawStacked = 1000
    clawRedHalfOpen = 1300
    clawGreenHalfOpen = 1450
    clawCrossed = 2047

    #Tophat
    FRONT_TOPHAT = 0
    onBlack = 3000

elif IS_CLONE_BLUE:
    # Servos
    servoClaw = 0

    # camera channels
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

    # color tolerances
    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 100

    # Claw position values
    clawOpen = 0
    clawAlmostOpen = 500
    clawHalfCrossed = 640
    clawMiddle = 650
    clawStacked = 1080
    clawRedHalfOpen = 1400
    clawGreenHalfOpen = 1550
    clawCrossed = 2047

    # Tophat
    FRONT_TOPHAT = 0
    onBlack = 3000

else:
    # Servos
    servoArm = 0
    servoClaw = 1


    # camera channels
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

    # color tolerances
    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 100

    # Claw position values
    # clawOpen = 0
    # clawAlmostOpen = 500
    # clawHalfCrossed = 640
    # clawMiddle = 650
    # clawStacked = 1080
    # clawRedHalfOpen = 1400
    # clawGreenHalfOpen = 1550
    # clawCrossed = 2047

    armUp = 760
    armBlockLevel = 1520
    armMid = 1450
    armDestack = 1100

    clawOpen = 750
    clawClosed = 150

    # Tophat
    FRONT_TOPHAT = 0
    onBlack = 3000