
class MathOp (object):

    __id__ = 0

    def __init__(self):
        self.result = None
        self.flow = None
        self.__id__ = 0
        self.__increment_id__()

    def __increment_id__(self):
        MathOp.__id__ = MathOp.__id__ + 1
        self.__id__ = MathOp.__id__

    def calculate(self):
        pass

    def backward(self, edge_value):
        pass


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

        return "%s + %s = %s" % (self.input_x, self.input_y, self.result)


class SubtractionOp(MathOp):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value - self.input_y.value

        return self.result

    def backward(self, edge_value):

        if edge_value == self.input_x:
            return 1

        return -1

    def __str__(self):

        return "%s - %s = %s" % ( self.input_x, self.input_y, self.result)


class DivideOp(MathOp):

    def __init__(self, x, y):
        self.input_x = x
        self.input_y = y

        super().__init__()

    def calculate(self):

        self.result = self.input_x.value / self.input_y.value

        return self.result

    def backward(self, edge_value):

        if edge_value == self.input_x:
            return 1 / self.input_y.value

        return edge_value.value / self.input_y.value ** 2

    def __str__(self):

        return "%s / %s = %s" % (self.input_x, self.input_y, self.result)


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
        if edge_value == self.input_x:
            return self.input_y.value

        return self.input_x.value

    def __str__(self):

        return "%s * %s = %s" % (self.input_x, self.input_y, self.result)


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