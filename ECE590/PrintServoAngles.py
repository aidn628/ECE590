from math import sin, cos, pi
from pylx16a.lx16a import *
import time
import platform

if(platform.system() == 'Windows'):
    LX16A.initialize("COM3")
else:
    LX16A.initialize("/dev/ttyUSB0")

def storeAngle(servo, servoAngles):
    try:
        a = servo.get_physical_angle()
        servoAngles[servo.get_id()] = a
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

    servoAngles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    while True:
        for servo in servos:
            print(f"Servo {servo.get_id()}: ", end="")
            storeAngle(servo, servoAngles)
        time.sleep(0.25)
        print(f"{servoAngles}\n\n")

if __name__ == "__main__":
    main()