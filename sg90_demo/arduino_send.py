import serial
import IK_3D

ser = Serial.serial(port="COM13", baudrate=115200)

def read():
    print(str(ser.readline().decode("utf")))
    
def write(val):
    ser.write(str(val).encode('utf-8'))

#TODO send table after solving and add accurate joint data