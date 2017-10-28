from .NxFlow import NxFlow
from .SnapFlow import SnapFlow


class FlowCreator(object):

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def default_creator(cls, name="default"):

        if "snap" in name:
            return SnapFlow()

        return NxFlow()

