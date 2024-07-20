import numpy as np

def linearTransformation(v, m):
    size = len(v)
    if (size != len(m)):
        print(f"Illegal vector and matrix sizes for transformation! (v={size}, m={len(m)})")
        return None
    return np.array([sum([v[i] * m[j][i] for i in range(size)]) for j in range(size)])

def globalPositionDerivative(joint_index, angle_index, joints):
    if (angle_index > joint_index): #Changing angles on joints "above" the current joint will not affect said joint
        return [0,0,0]
    last_pos = joints[angle_index].getLocalPositionDerivative()
    for j in range(angle_index):
        last_pos = linearTransformation(last_pos, joints[angle_index - j - 1].getRotationMatrix())

    #Could be a source of problems in the future; indexing is a bit strange
    #Equation on back page of pt 2
    summation = [0,0,0]
    for i in range(angle_index + 1, joint_index + 1):
        prod = joints[i].getLocalPosition()
        for j in range(i - angle_index - 1):
            prod = linearTransformation(prod, joints[i - j - 1].getRotationMatrix())
        prod = linearTransformation(prod, joints[angle_index].getRotationMatrixDerivative())
        for j in range(i - angle_index, i):
            prod = linearTransformation(prod, joints[i - j - 1].getRotationMatrix())
        summation += prod

    return last_pos + summation

def angleWrap(angle):
    if isinstance(angle, list):
        return [Solver.angleWrap(i) for i in angle]
    return angle - np.round(angle / (2 * np.pi)) * 2 * np.pi