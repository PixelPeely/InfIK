from IK_3D import *
 
ik_system = IKSystem(
    joints=[
        Joint(0.39, 0.76, 35, 33),
        Joint(-0.41, 0.45, 30, 35),
        Joint(0.55,-0.87, 32, 43),
    ],
    constraints=[
        Constraint(2, 0, 50),
        Constraint(2, 1, 50),
        Constraint(2, 2, 50)
    ]
)

print(Solver.solve(ik_system))
#The solutions can also be accessed directly from the Joint object:
print(ik_system.joints[2].theta)

#The absolute position of any joint is also available
ik_system.joints[0].setTheta(1)
print(ik_system.joints[2].getGlobalPosition(2, ik_system.joints))