from Joint import Joint
from Constraint import Constraint
import numpy as np
import Util
import time

joints = [
    Joint(0.39, 0.76, 1.17),
    Joint(-0.41, 0.45, 1),
    Joint(0.55,-0.87, 1.22),
]

constraints = [
    Constraint(2, 0, 0.1),
    Constraint(1, 1, 1.51),
    Constraint(2, 2, -1.56)
]

def constructJacobian():
    #Cache table
    constrained_joints = [c.joint_index for c in constraints]
    global_derivatives = {
        j:([Util.globalPositionDerivative(j, i, joints) for i in range(len(joints))]) for j in set(constrained_joints)
    }
    
    return np.array([[global_derivatives[row.joint_index][column][row.axis] for column in range(len(joints))] for row in constraints])

def constructFunctionTable():
    return np.array([joints[c.joint_index].getGlobalPosition(c.joint_index, joints)[c.axis] - c.value for c in constraints])

def convergePoint(guess):
    for i in range(len(guess)):
        joints[i].setPosition(guess[i])
    return guess - Util.linearTransformation(constructFunctionTable(), np.linalg.inv(constructJacobian()))

#print(constructJacobian())
#print(Util.globalPositionDerivative(2, 2, joints))
guess = [0,0,0]
guesses = []
start_t = time.time()
for i in range(100):
    guess = convergePoint(guess)
    guesses.append(guess)
end_t = time.time()
print(f"Converged in {(end_t - start_t) * 1000} ms")
for i in range(len(guesses)):
    print(f"{i}:{guesses[i]}")