import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 2
RMOTOR = 0

# Digital ports
ROBOT_ID_YELLOW = 0
ROBOT_ID_BLUE = 1

RIGHT_BUTTON = 13

# Analog ports


IS_YELLOW_BOT = w.digital(ROBOT_ID_YELLOW)
IS_BLUE_BOT = w.digital(ROBOT_ID_BLUE)
IS_ORANGE_BOT = not IS_YELLOW_BOT and not IS_BLUE_BOT


# Drive Constants
WHEEL_DISTANCE = 5.50 #205 - 4.25  # Distance between the two wheels


if IS_ORANGE_BOT:
    INCHES_TO_TICKS = 222 #192 #larger numbers = longer drive

    lAdjust =  1.02 #.86 #.875 # 1.12 # .99  # adjust left wheel counter to fix drift; Larger number makes the robot drive left...?
else: # Blue Bot
    INCHES_TO_TICKS = 204
    lAdjust = 1.125  # adjust left wheel counter to fix drift    #1.083

# Servos
if IS_ORANGE_BOT:
    #servoFrisbeeGrabber = 0
    servoClaw = 0
    servoArm = 2
    servoFrisbeeArm = 3
else: # Blue Bot
    servoClaw = 1
    servoArm = 2
    servoFrisbeeArm = 3

#camera channels
if IS_ORANGE_BOT:
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
else:  # Blue Bot
    ORANGE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3

#color tolerances
if IS_ORANGE_BOT:
    COLOR_PROXIMITY=20
    ORANGE_AREA=500
    RGY_AREA=100
else:  # Blue Bot
    COLOR_PROXIMITY = 20
    ORANGE_AREA = 500
    RGY_AREA = 100

#New claw posistion values
if IS_ORANGE_BOT:
    clawOpen = 1620
    clawFullyOpen = 1980
    clawClosed = 840 + 150
else:  # Blue Bot
    clawOpen = 870-15
    clawFullyOpen = 1550
    clawClosed = 20

#Arm posistion values0
if IS_ORANGE_BOT:
    armUp = 900
    armBlockLevel = 1580
    armMid = 1450
    armHighMid = 1300
    armDestack = 1030
    armFrisbee = 1491
    armStartBoxPosition = 800
else:  # Blue Bot
    armUp = 900
    armBlockLevel = 1580
    armMid = 1450
    armHighMid = 1300
    armDestack = 1030
    armFrisbee = 1491
    armStartBoxPosition = 800

#Frisbee arm posistion values
if IS_ORANGE_BOT:
    frisbeeArmUp = 1290
    frisbeeArmDown = 1950
    frisbeeArmGrab = 1256
    frisbeeArmPickUp = 1000
    frisbeeArmHorizontal = 1550
    frisbeeArmStartPosition = 870
else:  # Blue Bot
    frisbeeArmUp = 500
    frisbeeArmDown = 1168
    frisbeeArmGrab = 463
    frisbeeArmPickUp = 300
    frisbeeArmHorizontal = 850
    frisbeeArmStartPosition = 110

#Frisbee grabber posistion values
if IS_ORANGE_BOT:
    frisbeeGrabberClosed = 1910
    frisbeeGrabberOpen = 720
else:  # Blue Bot
    frisbeeGrabberClosed = 1910
    frisbeeGrabberOpen = 720

#Tophat
if IS_ORANGE_BOT:
    FRONT_TOPHAT = 0
    LEFT_TOPHAT = 1
    RIGHT_TOPHAT = 3
    BACK_TOPHAT= 5
    STARTLIGHT = 4
    TOPHAT_THRESHOLD = 2000
else: # Blue Bot
    FRONT_TOPHAT = 0
    LEFT_TOPHAT = 2
    RIGHT_TOPHAT = 1
    BACK_TOPHAT = 5
    STARTLIGHT = 3
    TOPHAT_THRESHOLD = 2000 #2700