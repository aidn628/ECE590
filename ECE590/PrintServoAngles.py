from math import sin, cos, pi
from pylx16a.lx16a import *
import time

LX16A.initialize("COM3")


def printAngle(servo1):
    try:
        print(f"{servo1.get_physical_angle():0.2f}°")
    except (ServoTimeoutError, ServoChecksumError):
        pass


def main():
    servos = []
    try:
        for i in range(1, 9):
            servos.append(LX16A(i))
    except ServoTimeoutError as e:
        print(f"Servo {e.id_} is not responding. Exiting...")
        quit()

    for servo in servos:
        servo.disable_torque()
    
    while True:
        for servo in servos:
            print(f"Servo {servo.get_id()}: ", end="")
            printAngle(servo)
        time.sleep(1)
        print("\n\n")

if __name__ == "__main__":
    main()