from Joint import Joint
from Constraint import Constraint
import Util

joints = [
    Joint(0.39, 0.79, 1.17),
    Joint(-0.41, 0.45, 1),
    Joint(0.55,-0.87, 1)
]

constraints = [
    Constraint(3, 0, 0.1),
    Constraint(3, 1, 1.51),
    Constraint(3, 2, -1.56)
]

