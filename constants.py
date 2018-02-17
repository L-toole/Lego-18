import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 3
RMOTOR = 0

# Digital ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

isClone = w.digital(CLONE_SWITCH)

# Servos
servoClaw = 0

#camera channels
ORANGE = 0
RED = 1
GREEN = 2
YELLOW = 3

#color tolerances
COLOR_PROXIMITY=20
ORANGE_AREA=1500
RGY_AREA=300

#Claw position values
clawCrossed = 2047
clawOpen = 0
clawMiddle = 650
clawRedHalfOpen = 1200
clawGreenHalfOpen = 1450
clawHalfCrossed = 640
clawStacked = 1000

#Tophat
FRONT_TOPHAT = 0
onBlack = 3000