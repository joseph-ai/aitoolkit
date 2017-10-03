
class MathRv (object):

    def __init__(self):
        self.value = None

    def calculate(self):
        pass

    def calcBackward(self):
        pass


class MultiplyRv(MathRv):

    def __init__(self, x, y):
        self.x = x
        self.y = y

        super().__init__()

    def calculate(self):

        self.value = self.x * self.y

        return self.value


class AdditionRv(MathRv):

    def __init__(self, x, y):
        self.x = x
        self.y = y

        super().__init__()

    def calculate(self):

        self.value = self.x + self.y

        return self.value

    def __str__(self):

        return "%s + %s=%s" % (self.x, self.y, self.value)


class IdentityRv(MathRv):

    def __init__(self, x):
        self.x = x
        self.value = None
        super().__init__()

    def calculate(self):
        self.value = self.x
        return self.x

    def __str__(self):

        return "Id(%s)=%s" % (self.x, self.value)
