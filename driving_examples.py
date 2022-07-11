from WPILib import *

#square function
def square(sidelength):
    for sides in range(4):
        driveBase.straight(sidelength)
        driveBase.turn(90)

#polygon function
def polygon(sides):
    for s in range(sides):
        driveBase.straight(150)
        driveBase.turn(360/sides)

def standoff():
    Kp = 0.2
    while True:
        distance = sonar.distance
        error = distance - 10.0
        driveBase.setEfforts(error * Kp)
        time.sleep(0.01)

def driveTillClose():
    while True:
        if sonar.distance > 10:
            driveBase.setEffort(0.60, 0.60)
        else:
            driveBase.setEffort(0, 0)
        time.sleep(0.01)

# Example using encoders of driving for a distance

# Example of turning using encoders

def lineTrack():
    baseEffort = 0.6
    Kp = 0.02
    while True:
        error = refl.right() - refl.left()
        driveBase.setEffort(0.6 + error * Kp, 0.6 - error * Kp)

driveBase = drv.drive()
lineTrack()

while True:
    print("Left:", refl.left(), "right:", refl.right())
    time.sleep(0.25)