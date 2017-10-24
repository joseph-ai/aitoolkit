import toolkit.autodiff.math as am

from ..CalcFlow import CalcFlow


class FloatRv(CalcFlow):

    def __init__(self, value):

        super().__init__(value)

    def _calc_binary(self, other, func):

        calc_val = FloatRv(func.calculate())

        self._add_edge_to_both(other, func)

        calc_val.network = self._compose(other)

        calc_val.last_node = func

        func.result = calc_val

        func.network = calc_val.network

        return calc_val

    def _calc_unary(self, func):

        calc_val = FloatRv(func.calculate())
        self._add_edge_to_self(func)
        calc_val.last_node = func
        calc_val.network = self.network
        func.result = calc_val
        func.network = calc_val.network
        return calc_val

    @classmethod
    def create(cls, value):

        v = FloatRv(value)

        math_func = am.IdentityRv(v)

        calc_val = v._calc_unary(math_func)

        calc_val.identity = math_func

        return calc_val

    def __mul__(self, other):

        if not CalcFlow.isCalcFlow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.MultiplyRv(self, other)

        return self._calc_binary(other, math_func)

    def __add__(self, other):

        if not CalcFlow.isCalcFlow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.AdditionRv(self, other)

        return self._calc_binary(other, math_func)

    def __sub__(self, other):

        if not CalcFlow.isCalcFlow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.SubtractionRv(self, other)

        return self._calc_binary(other, math_func)

    def __pow__(self, other):

        if not CalcFlow.isCalcFlow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.ExponentRv(self, other)

        return self._calc_binary(other, math_func)

    def __div__(self, other):

        if not CalcFlow.isCalcFlow(other):
            raise ValueError("Not CalcFlow")

        math_func = am.DivideRv(self, other)

        return self._calc_binary(other, math_func)

    def sin(self):

        math_func = am.SinRv(self)

        return self._calc_unary(math_func)

    def exp(self):

        math_func = am.ExpRv(self)

        return self._calc_unary(math_func)

    def ln(self):

        math_func = am.LnRv(self)

        return self._calc_unary(math_func)

    def __truediv__(self, other):

        return self.__div__(other)

    def __str__(self):

        return "%s" % self.value

