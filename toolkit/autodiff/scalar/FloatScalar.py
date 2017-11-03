import toolkit.autodiff.math.scalar as am
import toolkit.autodiff.math as m

from ..math import IdentityOp
from ..CalcFlow import CalcFlow


class FloatScalar(CalcFlow):

    def __init__(self, value):

        super().__init__(value)

    def _calc_unary(self, func):

        calc_val = FloatScalar(func.calculate())

        super(FloatScalar, self).__calc_unary__(calc_val, func)

        return calc_val

    def _calc_binary(self, other, func):

        calc_val = FloatScalar(func.calculate())

        super(FloatScalar, self).__calc_binary__(calc_val, other, func)

        return calc_val

    @classmethod
    def create(cls, value):

        v = FloatScalar(value)

        math_func = IdentityOp(v)

        calc_val = v._calc_unary(math_func)

        calc_val.identity = math_func

        return calc_val

    def __mul__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = m.MultiplyOp(self, other)

        return self._calc_binary(other, math_func)

    def __add__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = m.AdditionOp(self, other)

        return self._calc_binary(other, math_func)

    def __sub__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = m.SubtractionOp(self, other)

        return self._calc_binary(other, math_func)

    def __pow__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = m.ExponentOp(self, other)

        return self._calc_binary(other, math_func)

    def __div__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = m.DivideOp(self, other)

        return self._calc_binary(other, math_func)

    def sin(self):

        math_func = am.SinOp(self)

        return self._calc_unary(math_func)

    def exp(self):

        math_func = am.ExpOp(self)

        return self._calc_unary(math_func)

    def ln(self):

        math_func = am.LnOp(self)

        return self._calc_unary(math_func)

    def __truediv__(self, other):

        return self.__div__(other)

    def __str__(self):

        return "[%s] %s" % (self.__id__, self.value)

