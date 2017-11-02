
from ..flow import FlowCreator


class Module(object):
    """
    Base class to all nn modules
    """

    def __init__(self):

        # this is my network
        self.flow = FlowCreator.default_creator()
        self.flow.init()

    def forward(self, *args, **kwargs):
        """This should be over on all subclasses
        Defineds the computation performed at every call
        """

        raise NotImplementedError

    def apply(self, func):

        """Applies a function to every child and itself"""


