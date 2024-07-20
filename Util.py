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
    print(f"Differentiating local space of joint {angle_index}")
    last_pos = joints[angle_index].getLocalPositionDerivative()
    for j in range(angle_index):
        print(f"Transform1 {angle_index - j - 1}")
        last_pos = linearTransformation(last_pos, joints[angle_index - j - 1].getRotationMatrix())
    print("End prod")

    #Could be a source of problems in the future; indexing is a bit strange
    #Equation on back page of pt 2
    summation = [0,0,0]
    for i in range(angle_index + 1, joint_index + 1):
        print(f"Sumi: {i}")
        prod = joints[i].getLocalPosition()
        for j in range(i - angle_index - 1):
            prod = linearTransformation(prod, joints[i - j - 1].getRotationMatrix())
            print(f"Transform2 {i-j-1}")
        prod = linearTransformation(prod, joints[angle_index].getRotationMatrixDerivative())
        print(f"Transform3 {angle_index}")
        for j in range(i - angle_index, i):
            prod = linearTransformation(prod, joints[i - j - 1].getRotationMatrix())
            print(f"Transform4 {i-j-1}")
        print("End prod")
        summation += prod   
    print("End sum")

    return last_pos + summation