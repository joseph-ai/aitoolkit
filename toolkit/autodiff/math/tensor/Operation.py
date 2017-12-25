import numpy as np

from ..MathOp import MathOp


class SinOp(MathOp):

    def __init__(self, x):
        self.input_x = x

        super().__init__()

    def calculate(self):

        self.result = np.sin(self.input_x.value)

        return self.result

    def backward(self, edge_value):

        return np.cos(edge_value.value)

    def __str__(self):

        return "Sin(%s) = %s" % (self.input_x, self.result)


class ExpOp(MathOp):

    def __init__(self, x):
        self.input_x = x

        super().__init__()

    def calculate(self):

        self.result = np.exp(self.input_x.value)

        return self.result

    def backward(self, edge_value):

        return np.exp(edge_value)

    def __str__(self):

        return "e ** (%s) = %s" % ( self.input_x, self.result)


class LnOp(MathOp):

    def __init__(self, x):
        self.input_x = x

        super().__init__()

    def calculate(self):

        self.result = np.log(self.input_x.value)

        return self.result

    def backward(self, edge_value):

        return 1 / edge_value.value

    def __str__(self):

        return "ln(%s) = %s" % (self.input_x, self.result)


class DotProduct(MathOp):

    def __init__(self, m1, m2):

        self.input_m1 = m1
        self.input_m2 = m2
        super().__init__()

    def calculate(self):

        self.result = np.dot(self.input_m1, self.input_m2)
        return self.result

    def backward(self, edge_value):
        pass

    def __str__(self):

        return "np.dot(%s,%s) = %s" % (self.input_m1.shape, self.input_m2.shape, self.result.shape)

