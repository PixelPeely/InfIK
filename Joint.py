import numpy as np
import Util

class Joint:
    alpha = 0 
    beta = 0
    theta = 0
    length = 0
    
    sin_t = 0
    cos_t = 1
    sin_a = 0
    cos_a = 1
    sin_b = 0
    cos_b = 1
        

    def __init__(self, alpha, beta, length):
        self.alpha = alpha
        self.beta = beta
        self.length = length
        self.sin_a = np.sin(alpha)
        self.cos_a = np.cos(alpha)
        self.sin_b = np.sin(beta)
        self.cos_b = np.cos(beta)
    
    def setPosition(self, theta):
        self.theta = theta
        self.sin_t = np.sin(self.theta)
        self.cos_t = np.cos(self.theta)

    def getAxisVector(self):
        return np.array([
            self.cos_b * self.cos_a,
            self.cos_b * self.sin_a,
            self.sin_b
        ])

    def getUnitVector(self):
        return np.array([
            -self.sin_t * self.sin_b * self.cos_a - self.cos_t * self.sin_a,
            self.cos_t * self.cos_a - self.sin_t * self.sin_b * self.sin_a,
            self.sin_t * self.cos_b
        ])

    def getLocalPosition(self):
        return self.getUnitVector() * self.length

    def getGlobalPosition(self, self_index, joints):
        summation = [0,0,0]
        for i in range(self_index + 1):
            prod = joints[i].getLocalPosition()
            for j in range(i):
                prod = Util.linearTransformation(prod, joints[i - j - 1].getRotationMatrix())
            summation += prod
        return summation

    def getLocalPositionDerivative(self):
        return self.length * np.array([
            self.sin_t * self.sin_a - self.cos_t * self.sin_b * self.cos_a,
            - self.sin_t * self.cos_a - self.cos_t * self.sin_b * self.sin_a,
            self.cos_t * self.cos_b
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
        return np.array([
            [self.sin_t * self.sin_a - self.cos_t * self.sin_b * self.cos_a,
            a[1] * self.cos_t * self.cos_b + a[2] * (self.sin_t * self.cos_a + self.cos_t * self.sin_b * self.sin_a),
            0],
            [-self.sin_t * self.cos_a - self.cos_t * self.sin_b * self.sin_a,
            a[2] * (self.sin_t * self.sin_a - self.cos_t * self.sin_b * self.cos_a) - a[0] * self.cos_t * self.cos_b,
            0],
            [self.cos_t * self.cos_b,
            a[0] * (-self.sin_t * self.cos_a - self.cos_t * self.sin_b * self.sin_a) 
                - a[1] * (self.sin_t * self.sin_a - self.cos_t * self.sin_b * self.cos_a),
            0]
        ])