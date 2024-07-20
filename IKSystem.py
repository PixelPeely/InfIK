

class IKSystem:
    joints = []
    constraints = []
    allowed_error = 0

    def __init__(self, joints, constraints, allowed_error = 1e-10):
        self.joints = joints
        self.constraints = constraints
        self.allowed_error = allowed_error