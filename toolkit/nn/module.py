
from ..autodiff.math import MathOp


class Module(MathOp):
    """
    Base class to all nn modules
    """

    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        """This should be over on all subclasses
        Defineds the computation performed at every call
        """

        raise NotImplementedError

    def apply(self, func):

        """Applies a function to every child and itself"""


