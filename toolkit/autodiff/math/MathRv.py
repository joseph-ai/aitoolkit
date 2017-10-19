import math


class MathRv (object):

    def __init__(self):
        self.result = None
        self.network = None

    def calculate(self):
        pass

    def backwards(self, edge_value):
        pass


class MultiplyRv(MathRv):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value * self.input_y.value

        return self.result

    def backwards(self, edge_value):

        # the partial derivative with respect to either input x or y
        if edge_value == self.input_x.value:
            return self.input_y

        return self.input_x

    def __str__(self):

        return "%s * %s = %s" % (self.input_x, self.input_y, self.result)


class AdditionRv(MathRv):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value + self.input_y.value

        return self.result

    def backwards(self, edge_value):

        # the partial derivative with respect to either input x or y
        if edge_value == self.input_x.value:
            return self.input_x

        return self.input_y

    def __str__(self):

        return "%s + %s = %s" % (self.input_x, self.input_y, self.result)


class ExponentRv(MathRv):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value ** self.input_y.value

        return self.result

    def __str__(self):

        return "%s ^ %s = %s" % (self.input_x, self.input_y, self.result)



class SubtractionRv(MathRv):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value - self.input_y.value

        return self.result

    def __str__(self):

        return "%s - %s = %s" % (self.input_x, self.input_y, self.result)


class DivideRv(MathRv):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value / self.input_y.value

        return self.result

    def __str__(self):

        return "%s / %s = %s" % (self.input_x, self.input_y, self.result)


class SinRv(MathRv):

    def __init__(self, x):
        self.input_x = x

        super().__init__()

    def calculate(self):

        self.result = math.sin(self.input_x.value)

        return self.result

    def backwards(self, edge_value):

        return math.cos(edge_value)

    def __str__(self):

        return "sin(%s) = %s" % (self.input_x, self.result)


class ExpRv(MathRv):

    def __init__(self, x):
        self.input_x = x

        super().__init__()

    def calculate(self):

        self.result = math.exp(self.input_x.value)

        return self.result

    def backwards(self, edge_value):

        return math.exp(edge_value)

    def __str__(self):

        return "e ** (%s) = %s" % (self.input_x, self.result)


class LnRv(MathRv):

    def __init__(self, x):
        self.input_x = x

        super().__init__()

    def calculate(self):

        self.result = math.log(self.input_x.value)

        return self.result

    def backwards(self, edge_value):

        return edge_value * 1/edge_value

    def __str__(self):

        return "ln(%s) = %s" % (self.input_x, self.result)


class IdentityRv(MathRv):

    def __init__(self, x):
        self.input_x = x
        self.result = None
        super().__init__()

    def calculate(self):
        self.result = self.input_x
        return self.input_x.value

    def backwards(self, value=None, seed=None):
        return 0

    def __str__(self):

        return "Id(%s) = %s" % (self.input_x, self.result)
