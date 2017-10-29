import toolkit.autodiff.math.tensor as am

from ..math import IdentityOp
from ..CalcFlow import CalcFlow


class FloatTensor(CalcFlow):

    def __init__(self, value):

        super().__init__(value)

    def _calc_unary(self, func):

        calc_val = FloatTensor(func.calculate())

        super(FloatTensor, self).__calc_unary__(calc_val, func)

        return calc_val

    def _calc_binary(self, other, func):

        calc_val = FloatTensor(func.calculate())

        super(FloatTensor, self).__calc_binary__(calc_val, other, func)

        return calc_val

    @classmethod
    def create(cls, value):

        v = FloatTensor(value)

        math_func = IdentityOp(v)

        calc_val = v._calc_unary(math_func)

        calc_val.identity = math_func

        return calc_val
