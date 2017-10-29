from .MathOp import MathOp


class IdentityOp(MathOp):

    def __init__(self, x):
        self.input_x = x
        self.result = None
        super().__init__()

    def calculate(self):
        return self.input_x.value

    def backward(self, edge_value):
        return 0

    def __str__(self):

        return "Id(%s) = %s" % (self.input_x, self.result)