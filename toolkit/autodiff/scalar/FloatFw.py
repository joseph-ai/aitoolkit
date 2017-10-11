
class FloatFw(object):

    def __init__(self, val, delta):

        # current value
        self.val = val

        # this is the derivative of the previous function
        self.delta = delta

    def __add__(self, other):
        val = self.val + other.val
        delta = self.delta + other.delta

        return FloatFw(val, delta)

    def __mul__(self, other):

        # [ product rule ] f * g = f'*g + g' * f

        val = self.val * other.val

        delta = other.val * self.delta + self.val * other.delta

        return FloatFw(val, delta)
