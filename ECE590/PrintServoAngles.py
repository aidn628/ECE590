from math import sin, cos, pi
from pylx16a.lx16a import *
import time
import platform
from curtsies import Input

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

    f = open("testfile.csv", "w")

    servoAngles = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    while True:
        with Input(keynames='curses') as input_generator:
            for e in input_generator:
                #print(repr(e))
                if e == ' ':
                    fstr = f"{servoAngles[0]},{servoAngles[1]},{servoAngles[2]},{servoAngles[3]},{servoAngles[4]},{servoAngles[5]},{servoAngles[6]},{servoAngles[7]},{servoAngles[8]}\n"
                    print(f"written {fstr} to file")
                    f.write(fstr)
                else:
                    for servo in servos:
                        storeAngle(servo, servoAngles)
                    print(f"{servoAngles}")
                    time.sleep(0.02)

    

if __name__ == "__main__":
    main()