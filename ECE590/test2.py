from math import sin, cos, pi
from pylx16a.lx16a import *
import time

LX16A.initialize("COM3")

#SERVO      HOME OFFSET
#servo 1 is 90 -13.5
#servo 2 is 141.5 0
#servo 3 is 90 18

S1_HOME = 90
S1_OFFSET = -13.5
S1_LLIM = 20
S1_RLIM = 160

S2_HOME = 145
S2_OFFSET = 0
S2_LLIM = 115
S2_RLIM = 170

S3_HOME = 90
S3_OFFSET = 18
S3_LLIM = 0
S3_RLIM = 180

def printAngle(servo1):
    try:
        print(f"{servo1.get_physical_angle():0.2f}°")
    except (ServoTimeoutError, ServoChecksumError):
        pass


def main():
    try:
        servo1 = LX16A(1)
        servo1.set_angle_limits(S1_LLIM, S1_RLIM)
        servo1.set_angle_offset(S1_OFFSET)

        servo2 = LX16A(2)
        servo2.set_angle_limits(S2_LLIM, S2_RLIM)
        servo2.set_angle_offset(S2_OFFSET)
    except ServoTimeoutError as e:
        print(f"Servo {e.id_} is not responding. Exiting...")
        quit()

    servo1.enable_torque()
    servo2.enable_torque()

    #Set all servos home
    servo1.move(S1_HOME, 2)
    servo2.move(S2_HOME, 2)
    time.sleep(1)

    servo1.move(S1_HOME, 1)
    servo2.move(S2_HOME, 1)
    time.sleep(1)

    servo2.move(120, 1)
    time.sleep(1)
    
    while True:
        servo1.move(150, 1)
        servo2.move(165,1)
        time.sleep(1)
        servo1.move(30, 1)
        time.sleep(1)
        servo1.move(90, 1)
        servo2.move(120,1)
        time.sleep(1)

if __name__ == "__main__":
    main()