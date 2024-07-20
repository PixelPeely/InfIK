import Solver
from Joint import Joint
from IKSystem import IKSystem
from Constraint import Constraint

ik_system = IKSystem(
    joints=[
        Joint(0.39, 0.76, 1.17),
        Joint(-0.41, 0.45, 1),
        Joint(0.55,-0.87, 1.22),
    ],
    constraints=[
        Constraint(2, 0, 0.1),
        Constraint(2, 1, 1.51),
        Constraint(2, 2, -1.56)
    ]
)

print(Solver.solve(ik_system))