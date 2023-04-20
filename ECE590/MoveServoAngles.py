from pylx16a.lx16a import *
import time
import platform
import csv

if(platform.system() == 'Windows'):
    LX16A.initialize("COM3")
else:
    LX16A.initialize("/dev/ttyUSB0")

#SERVO      HOME OFFSET
#servo 1 is 90 -13.5
#servo 2 is 141.5 0
#servo 3 is 90 18

S1_HOME = 90
S1_OFFSET = -13.5
S1_LLIM = 30
S1_RLIM = 160

S2_HOME = 143
S2_OFFSET = 0
S2_LLIM = 110
S2_RLIM = 180

S3_HOME = 109
S3_OFFSET = 0
S3_LLIM = 45
S3_RLIM = 170

S4_HOME = 46.5
S4_OFFSET = -30
S4_LLIM = 18
S4_RLIM = 82

S5_HOME = 90
S5_OFFSET = -6
S5_LLIM = 25
S5_RLIM = 150

S6_HOME = 90
S6_OFFSET = 18
S6_LLIM = 60
S6_RLIM = 130

S7_HOME = 86.4
S7_OFFSET = 0
S7_LLIM = 25
S7_RLIM = 150

S8_HOME = 117.5
S8_OFFSET = 18
S8_LLIM = 80
S8_RLIM = 145

SERVO_HOMES = [0, S1_HOME, S2_HOME, S3_HOME, S4_HOME, S5_HOME, S6_HOME, S7_HOME, S8_HOME]
SERVO_OFFSETS = [0, S1_OFFSET, S2_OFFSET, S3_OFFSET, S4_OFFSET, S5_OFFSET, S6_OFFSET, S7_OFFSET, S8_OFFSET]
SERVO_LOWER_LIMITS = [0, S1_LLIM, S2_LLIM, S3_LLIM, S4_LLIM, S5_LLIM, S6_LLIM, S7_LLIM, S8_LLIM]
SERVO_UPPER_LIMITS = [0, S1_RLIM, S2_RLIM, S3_RLIM, S4_RLIM, S5_RLIM, S6_RLIM, S7_RLIM, S8_RLIM]


def main():
    servos = []
    try:
        for i in range(1, 9):
            servos.append(LX16A(i))
            servos[i-1].set_angle_limits(SERVO_LOWER_LIMITS[i], SERVO_UPPER_LIMITS[i])
            servos[i-1].set_angle_offset(SERVO_OFFSETS[i])
    except ServoTimeoutError as e:
        print(f"Servo {e.id_} is not responding. Exiting...")
        quit()

    for servo in servos:
        servo.enable_torque()

    #Set all servos home
    for servo in servos:
        servo.move(SERVO_HOMES[servo.get_id()], 3)
    time.sleep(2)

    for servo in servos:
        servo.move(SERVO_HOMES[servo.get_id()], 3)
    time.sleep(2)

    with open('testfile.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))

    for row in data:
        servos[0].move(float(row[1]), 50)
        servos[1].move(float(row[2]), 50)
        servos[2].move(float(row[3]), 50)
        servos[3].move(float(row[4]), 50)
        servos[4].move(float(row[5]), 50)
        servos[5].move(float(row[6]), 50)
        servos[6].move(float(row[7]), 50)
        servos[7].move(float(row[8]), 50)
        
        time.sleep((int(row[0]))/1000)

if __name__ == "__main__":
    main()