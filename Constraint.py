class Constraint:
    joint_index = 0
    axis = 0 #0=x, 1=y, 2=z
    value = 0

    def __init__(self, joint_index, axis, value):
        self.joint_index = joint_index
        self.axis = axis
        self.value = value