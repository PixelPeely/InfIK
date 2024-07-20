from Joint import Joint
from Constraint import Constraint
from IKSystem import IKSystem
import numpy as np
import Util
import time

def constructJacobian(ik_system):
    #Cache table
    constrained_joints = [c.joint_index for c in ik_system.constraints]
    global_derivatives = {
        j:([Util.globalPositionDerivative(j, i, ik_system.joints) for i in range(len(ik_system.joints))]) for j in set(constrained_joints)
    }
    
    return np.array([[global_derivatives[row.joint_index][column][row.axis] for column in range(len(ik_system.joints))] for row in ik_system.constraints])

def constructFunctionTable(ik_system):
    return np.array([ik_system.joints[c.joint_index].getGlobalPosition(c.joint_index, ik_system.joints)[c.axis] - c.value for c in ik_system.constraints])

def convergePoint(guess, ik_system):
    updateJointPositions(guess, ik_system)
    return guess - Util.linearTransformation(constructFunctionTable(ik_system), np.linalg.inv(constructJacobian(ik_system)))

def updateJointPositions(pos_set, ik_system):
    for i in range(len(pos_set)):
        ik_system.joints[i].setPosition(pos_set[i])

def solve(ik_system):
    """
    Solve the system of joints to adhere to the given constraints
    Returns an array containing the angles of every joint in the system in the same order as the joint table
    -You can also read these directly from the joint table of your IKSystem
    """
    guess = [0,0,0]
    start_t = time.time()
    for i in range(100):
        lastGuess = guess
        guess = convergePoint(guess, ik_system)
        if ((np.abs(lastGuess - guess) < ik_system.allowed_error).all()):
            break
        if (i == 99):
            print(f"Solver failed to converge! Last guess difference was {guess-lastGuess}, but the minimum is {allowed_error}")
    end_t = time.time()
    print(f"Solver finished in {(end_t - start_t) * 1000} ms")
    guess = Util.angleWrap(guess)
    updateJointPositions(guess, ik_system)
    return guess