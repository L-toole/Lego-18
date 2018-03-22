import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 3
RMOTOR = 0

# Digital ports
ROBOT_ID_YELLOW = 0
ROBOT_ID_BLUE = 1

RIGHT_BUTTON = 13

#Analog ports


IS_YELLOW_BOT = w.digital(ROBOT_ID_YELLOW)
IS_BLUE_BOT = w.digital(ROBOT_ID_BLUE)
IS_ORANGE_BOT = not IS_YELLOW_BOT and not IS_BLUE_BOT


if IS_ORANGE_BOT:
    #Prime has new servo ports because of frisbee grab

    # Servos
    #servoFrisbeeGrabber = 0
    servoClaw = 1
    servoArm = 2
    servoFrisbeeArm = 0

    #camera channels
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

    #color tolerances
    COLOR_PROXIMITY=20
    ORANGE_AREA=500
    RGY_AREA=100

    #Claw position values (OLD CLAW!)
    # clawOpen = 0
    # clawAlmostOpen= 500
    # clawHalfCrossed = 640
    # clawMiddle = 650
    # clawStacked = 1000
    # clawRedHalfOpen = 1300
    # clawGreenHalfOpen = 1450
    # clawCrossed = 2047

    #New claw posistion values
    clawOpen = 1400
    clawFullyOpen = 1800
    clawClosed = 840

    #Arm posistion values
    armUp = 900
    armBlockLevel = 1580
    armMid = 1450
    armHighMid = 1300
    armDestack = 1030
    armFrisbee = 1491
    armStartBoxPosition = 800

    #Frisbee arm posistion values
    frisbeeArmUp = 1290
    frisbeeArmDown = 1980
    frisbeeArmGrab = 1256
    frisbeeArmStartPosition = 884

    #Frisbee grabber posistion values
    frisbeeGrabberClosed = 1910
    frisbeeGrabberOpen = 720


    #Tophat
    FRONT_TOPHAT = 0
    SIDE_TOPHAT = 1
    TOPHAT_THRESHOLD = 2000

elif IS_BLUE_BOT:
    # Servos
    servoClaw = 1
    servoFrisbeeGrabber = 2
    servoArm = 3
    servoFrisbeeArm = 2

    # camera channels
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

    # color tolerances
    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 100

    #New claw posistion values
    clawOpen = 1500
    clawFullyOpen = 1800
    clawClosed = 840

    #Arm posistion values
    armUp = 900
    armBlockLevel = 1580
    armMid = 1450
    armHighMid = 1300
    armDestack = 1030
    armFrisbee = 1491
    armStartBoxPosition = 800

    #Frisbee arm posistion values
    frisbeeArmUp = 1290
    frisbeeArmDown = 1980
    frisbeeArmGrab = 1450
    frisbeeArmStartPosition = 720

    #Frisbee grabber posistion values
    frisbeeGrabberClosed = 1910
    frisbeeGrabberOpen = 720

    # Claw position values (OLD CLAW!)
    # clawOpen = 0
    # clawAlmostOpen = 500
    # clawHalfCrossed = 640
    # clawMiddle = 650
    # clawStacked = 1080
    # clawRedHalfOpen = 1400
    # clawGreenHalfOpen = 1550
    # clawCrossed = 2047

    # Tophat
    FRONT_TOPHAT = 0
    TOPHAT_THRESHOLD = 3000

else: #IS_YELLOW_BOT
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

    # Claw position values (OLD CLAW!)
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
    armTilted = 1300

    clawOpen = 750
    clawClosed = 150

    # Tophat
    FRONT_TOPHAT = 0
    onBlack = 2000
    TOPHAT_THRESHOLD = 3000
