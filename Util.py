import numpy as np

def linearTransformation(v, m):
    size = len(v)
    if (size != len(m)):
        print(f"Illegal vector and matrix sizes for transformation! (v={size}, m={len(m)})")
        return None
    return np.array([sum([v[i] * m[j][i] for i in range(size)]) for j in range(size)])

def globalPositionDerivative(joint_index, angle_index, joints):
    joint = joints[joint_index]
    last_pos = joint.getLocalPositionDerivative()
    for j in range(angle_index):
        last_pos = linearTransformation(last_pos, joints[angle_index - j].getRotationMatrixDerivative())
    
    sumation = [0,0,0]
    for i in range(angle_index, joint_index):
        prod = joints[i].getLocalPosition()
        for j in range(i - angle_index):
            prod = linearTransformation(prod, joints[i - j].getRotationMatrix())
        prod = linearTransformation(prod, joints[angle_index].getRotationMatrixDerivative())
        for j in range(i - angle_index, i):
            prod = linearTransformation(prod, joints[i - j].getRotationMatrix())
        sumation += prod    

    return last_pos #+ sumation