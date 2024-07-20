from IK_3D import *
 
ik_system = IKSystem(
    joints=[
        Joint(0.39, 0.76, 1.17),
        Joint(-0.41, 0.45, 1),
        Joint(0.55,-0.87, 1.22),
    ],
    constraints=[
        Constraint(2, 0, 1),
        Constraint(2, 1, 1),
        Constraint(2, 2, 1)
    ]
)

print(Solver.solve(ik_system))
#You can also access these numbers directly from the Joint object:
print(ik_system.joints[2].theta)

#The absolute position of any servo is also available
ik_system.joints[0].setPosition(1)
print(ik_system.joints[2].getGlobalPosition(2, ik_system.joints))