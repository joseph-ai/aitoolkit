import math

from ..MathOp import MathOp


class SinOp(MathOp):

    def __init__(self, x):
        self.input_x = x

        super().__init__()

    def calculate(self):

        self.result = math.sin(self.input_x.value)

        return self.result

    def backward(self, edge_value):

        return math.cos(edge_value.value)

    def __str__(self):

        return "[%s] sin(%s) = %s" % (self.__id__, self.input_x, self.result)


class ExpOp(MathOp):

    def __init__(self, x):
        self.input_x = x

        super().__init__()

    def calculate(self):

        self.result = math.exp(self.input_x.value)

        return self.result

    def backward(self, edge_value):

        return math.exp(edge_value)

    def __str__(self):

        return "[%s] e ** (%s) = %s" % (self.__id__, self.input_x, self.result)


class LnOp(MathOp):

    def __init__(self, x):
        self.input_x = x

        super().__init__()

    def calculate(self):

        self.result = math.log(self.input_x.value)

        return self.result

    def backward(self, edge_value):

        return 1 / edge_value.value

    def __str__(self):

        return "[%s] ln(%s) = %s" % (self.__id__, self.input_x, self.result)

