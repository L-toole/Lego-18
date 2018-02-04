import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 0
RMOTOR = 3

# Digital ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

isClone = w.digital(CLONE_SWITCH)

# Servos
servoArm = 1
servoClaw = 0

armUp = 770
armDown = 900
armPickUp = 1425

clawCrossed = 0
clawOpen = 1740
clawMiddle = 600


