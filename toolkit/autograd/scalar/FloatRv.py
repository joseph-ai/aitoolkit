import toolkit.autograd.math as am
import networkx as nx

from ..CalcFlow import CalcFlow


class FloatRv(CalcFlow):

    def __init__(self, value):

        super().__init__(value)

    def __mul__(self, other):

        if not isinstance(other, CalcFlow):
            raise ValueError("Pass value that is not of derived type CalcFlow")

        math_func = am.MultiplyRv(self.value, other.value)

        return self._calc_binary(other, math_func)

    def __add__(self, other):

        if not isinstance(other, CalcFlow):
            raise ValueError("Pass value that is not of derived type CalcFlow")

        math_func = am.AdditionRv(self.value, other.value)

        return self._calc_binary(other, math_func)

    def _calc_binary(self, other, func):

        calc_val = FloatRv(func.calculate())

        self._add_edge_to_both(other, func)

        calc_val.network = self._compose(other)

        calc_val.last_node = func

        return calc_val

    def _calc_unary(self, func):

        calc_val = func.calculate()

        self._add_edge_to_self(func)

        self.last_node = func

        return calc_val

    @classmethod
    def create(cls, value):

        v = FloatRv(value)

        math_func = am.IdentityRv(v)

        return v._calc_unary(math_func)

    def __str__(self):

        return "%s" % self.value

