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


class MultiplyOp(MathOp):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value * self.input_y.value

        return self.result

    def backward(self, edge_value):

        # the partial derivative with respect to either input x or y
        if (edge_value.value == self.input_x.value).all():
            return self.input_y.value

        return self.input_x.value

    def __str__(self):

        return "%s * %s = %s" % (self.input_x, self.input_y, self.result)


class AdditionOp(MathOp):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value + self.input_y.value

        return self.result

    def backward(self, edge_value):

        # the partial derivative with respect to either input x or y is 1
        return 1

    def __str__(self):

        return "%s + %s = %s" % ( self.input_x, self.input_y, self.result)


class DivideOp(MathOp):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value / self.input_y.value

        return self.result

    def backward(self, edge_value):

        if (edge_value.value == self.input_x.value).any():
            return 1 / self.input_y.value

        return edge_value.value / self.input_y.value ** 2

    def __str__(self):

        return "%s / %s = %s" % (self.input_x, self.input_y, self.result)


class SubtractionOp(MathOp):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value - self.input_y.value

        return self.result

    def backward(self, edge_value):

        if (edge_value.value == self.input_x.value).all():
            return 1

        return -1

    def __str__(self):

        return "%s - %s = %s" % ( self.input_x, self.input_y, self.result)


class ExponentOp(MathOp):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value ** self.input_y.value

        return self.result

    def backward(self, edge_value):

        coeff = self.input_y.value
        expon = coeff - 1
        x = self.input_x.value

        return coeff * (x ** expon)

    def __str__(self):

        return "%s ^ %s = %s" % (self.input_x, self.input_y, self.result)
