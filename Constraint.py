class Constraint:
    joint_index = 1
    axis = 0 #0=x, 1=y, 2=z
    value = 1

    def __init__(self, joint_index, axis, value):
        self.joint_index = joint_index
        self.axis = axis
        self.value = value