import numpy as np

class Joint:
    alpha = 0 
    beta = 0
    theta = 0
    length = 0
    
    class Trig_Table:
        sin_t = 0
        cos_t = 0
        sin_a = 0
        cos_a = 0
        sin_b = 0
        cos_b = 0

        def init(self, joint):
            self.sin_a = np.sin(joint.alpha)
            self.cos_a = np.cos(joint.alpha)
            self.sin_b = np.sin(joint.beta)
            self.cos_b = np.cos(joint.beta)
        
        def updateTheta(self, theta):
            self.sin_t = np.sin(joint.theta)
            self.cos_t = np.cos(joint.theta)
    trig_table = Trig_Table()

    def __init__(self, alpha, beta, length):
        self.alpha = alpha
        self.beta = beta
        self.length = length
        self.trig_table.init(self)
    
    def setPosition(self, theta):
        self.theta = theta
        self.trig_table.updateTheta(theta)

    def getUnitVector(self):
        trig = self.trig_table
        return np.array([
            -trig.sin_t * trig.sin_b * trig.cos_a - trig.cos_t * trig.sin_a,
            trig.cos_t * trig.cos_a - trig.sin_t * trig.sin_b * trig.sin_a,
            trig.sin_t * trig.cos_b])

    def getLocalPosition(self):
        return self.getUnitVector() * self.length

    def getLocalPositionDerivative():
        return 0


joint = Joint(0.39, 0.76, 1.17)
joint.setPosition(-1.16)
print(joint.getLocalPosition())