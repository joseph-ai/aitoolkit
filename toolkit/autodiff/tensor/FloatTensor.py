import toolkit.autodiff.math as am

from ..CalcFlow import CalcFlow


class FloatTensor(CalcFlow):

    def __init__(self, value):

        super().__init__(value)


