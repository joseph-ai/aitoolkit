import toolkit.autodiff.math as am

from ..CalcFlow import CalcFlow


class FloatScalar(CalcFlow):

    def __init__(self, value):

        super().__init__(value)

    def _calc_binary(self, other, func):

        calc_val = FloatScalar(func.calculate())

        self._add_edge_to_both(other, func)

        calc_val.network = self._compose(other)

        calc_val.last_node = func

        func.result = calc_val

        func.network = calc_val.network

        return calc_val

    def _calc_unary(self, func):

        calc_val = FloatScalar(func.calculate())
        self._add_edge_to_self(func)
        calc_val.last_node = func
        calc_val.network = self.network
        func.result = calc_val
        func.network = calc_val.network
        return calc_val

    @classmethod
    def create(cls, value):

        v = FloatScalar(value)

        math_func = am.IdentityOp(v)

        calc_val = v._calc_unary(math_func)

        calc_val.identity = math_func

        return calc_val

    def __mul__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.MultiplyOp(self, other)

        return self._calc_binary(other, math_func)

    def __add__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.AdditionOp(self, other)

        return self._calc_binary(other, math_func)

    def __sub__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.SubtractionOp(self, other)

        return self._calc_binary(other, math_func)

    def __pow__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.ExponentOp(self, other)

        return self._calc_binary(other, math_func)

    def __div__(self, other):

        if not CalcFlow.is_calc_flow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.DivideOp(self, other)

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

        return "%s" % self.value

