import serial
import sys
sys.path.append('../')
from IK_3D import *

ser = serial.Serial(port="/dev/ttyACM0", baudrate=115200)

def read():
    print(str(ser.readline().decode("utf")))
    
def write(val):
    ser.write(str(val).encode('utf-8'))

# ik_system = IKSystem(
#     joints=[
#         Joint(0.39, 0.79, 60, 75),
#         Joint(-0.41, 0.45, 43, 57),
#         Joint(0.55, -0.87, 30, 60)
#     ],
#     constraints=[

#     ]
# )