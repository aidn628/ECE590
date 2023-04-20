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

S1_HOME = 120
S1_OFFSET = 0
S1_LLIM = 105
S1_RLIM = 206

S2_HOME = 168
S2_OFFSET = 0
S2_LLIM = 39
S2_RLIM = 198

S3_HOME = 145
S3_OFFSET = 0
S3_LLIM = 70
S3_RLIM = 225

S4_HOME = 143
S4_OFFSET = 0
S4_LLIM = 47
S4_RLIM = 153

S5_HOME = 179
S5_OFFSET = 0
S5_LLIM = 47
S5_RLIM = 210

S6_HOME = 166
S6_OFFSET = 0
S6_LLIM = 90
S6_RLIM = 222

S7_HOME = 195
S7_OFFSET = 0
S7_LLIM = 133
S7_RLIM = 233

SERVO_HOMES = [0, S1_HOME, S2_HOME, S3_HOME, S4_HOME, S5_HOME, S6_HOME, S7_HOME]
SERVO_OFFSETS = [0, S1_OFFSET, S2_OFFSET, S3_OFFSET, S4_OFFSET, S5_OFFSET, S6_OFFSET, S7_OFFSET]
SERVO_LOWER_LIMITS = [0, S1_LLIM, S2_LLIM, S3_LLIM, S4_LLIM, S5_LLIM, S6_LLIM, S7_LLIM]
SERVO_UPPER_LIMITS = [0, S1_RLIM, S2_RLIM, S3_RLIM, S4_RLIM, S5_RLIM, S6_RLIM, S7_RLIM]


def main():
    servos = []
    try:
        for i in range(1, 8):
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
        
        time.sleep((int(row[0]))/1000)

if __name__ == "__main__":
    main()