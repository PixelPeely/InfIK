import numpy as np
import Util

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

    def getAxisVector(self):
        trig = self.trig_table
        return np.array([
            trig.cos_b * trig.cos_a,
            trig.cos_b * trig.sin_a,
            trig.sin_b
        ])

    def getUnitVector(self):
        trig = self.trig_table
        return np.array([
            -trig.sin_t * trig.sin_b * trig.cos_a - trig.cos_t * trig.sin_a,
            trig.cos_t * trig.cos_a - trig.sin_t * trig.sin_b * trig.sin_a,
            trig.sin_t * trig.cos_b
        ])

    def getLocalPosition(self):
        return self.getUnitVector() * self.length

    def getLocalPositionDerivative(self):
        trig = self.trig_table
        return self.length * np.array([
            trig.sin_t * trig.sin_a - trig.cos_t * trig.sin_b * trig.cos_a,
            - trig.sin_t * trig.cos_a - trig.cos_t * trig.sin_b * trig.sin_a,
            trig.cos_t * trig.cos_b
        ])

    def getRotationMatrix(self):
        r = self.getUnitVector()
        a = self.getAxisVector()
        return np.array([
            [r[0], a[1] * r[2] - a[2] * r[1], a[0]],
            [r[1], a[2] * r[0] - a[0] * r[2], a[1]],
            [r[2], a[0] * r[1] - a[1] * r[0], a[2]]
        ])

    def getRotationMatrixDerivative(self):
        r = self.getUnitVector()
        a = self.getAxisVector()
        trig = self.trig_table
        return np.array([
            [trig.sin_t * trig.sin_a - trig.cos_t * trig.sin_b * trig.cos_a,
            a[1] * trig.cos_t * trig.cos_b + a[2] * (trig.sin_t * trig.cos_a + trig.cos_t * trig.sin_b * trig.sin_a),
            0],
            [-trig.sin_t * trig.cos_a - trig.cos_t * trig.sin_b * trig.sin_a,
            a[2] * (trig.sin_t * trig.sin_a - trig.cos_t * trig.sin_b * trig.cos_a) - a[0] * trig.cos_t * trig.cos_b,
            0],
            [trig.cos_t * trig.cos_b,
            a[0] * (-trig.sin_t * trig.cos_a - trig.cos_t * trig.sin_b * trig.sin_a) 
                - a[1] * (trig.sin_t * trig.sin_a - trig.cos_t * trig.sin_b * trig.cos_a),
            0]
        ])