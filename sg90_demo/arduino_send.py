import serial
import sys
import time
sys.path.append('../')
print(sys.path)
from IK_3D.IK_3D import *

#Change the port to the serial COM of your arduino
ser = serial.Serial(port="/dev/ttyACM0", baudrate=115200)

ik_system = IKSystem(
    joints=[
        Joint(0.39, 0.76, 60, 75),
        Joint(-0.41, 0.45, 43, 57),
        Joint(0.55, -0.87, 30, 60)
    ],
    constraints=[
        #set during runtime
    ],
)

constraint_sequence = [
    [
        Constraint(2, 0, 75),
        Constraint(2, 1, 75),
        Constraint(2, 2, 150)
    ],
    [
        Constraint(2, 0, 0),
        Constraint(2, 1, 75),
        Constraint(2, 2, 150)
    ],
    [
        Constraint(2, 0, 25),
        Constraint(2, 1, 100),
        Constraint(2, 2, 50)
    ],
    [
        Constraint(2, 0, 125),
        Constraint(2, 1, -25),
        Constraint(2, 2, 125)
    ],
    [
        Constraint(2, 0, 125),
        Constraint(2, 1, -75),
        Constraint(2, 2, 100)
    ],
    [
        Constraint(1, 0, 25),
        Constraint(2, 1, -50),
        Constraint(2, 2, 150)
    ],
    [
        Constraint(0, 1, 50),
        Constraint(1, 0, 0),
        Constraint(2, 2, 175)
    ],
    [
        Constraint(0, 2, 75),
        Constraint(1, 2, 130),
        Constraint(2, 2, 175)
    ],
    [
        Constraint(0, 1, -20),
        Constraint(2, 1, 25),
        Constraint(2, 2, 150)
    ]
]

time.sleep(5)
#To avoid hardware damage, it is recommended to only use values obtained from a successfull convergence.
#If the solver fails to converge, the output may be random and sporadic, which will be reflected by sudden and unpredictable movements.
for constraint in constraint_sequence:
    time.sleep(3)
    ik_system.constraints = constraint
    solution, success = Solver.solve(ik_system)
    if (success):
        print(f"Solution: {solution}")
        ser.write(','.join([str(round(i,3)) for i in solution]).encode("utf-8"))