
class MathOp (object):

    __id__ = 0

    def __init__(self):
        self.result = None
        self.flow = None
        self.__id__ = 0
        self.__increment_id__()

    def __increment_id__(self):
        MathOp.__id__ = MathOp.__id__ + 1
        self.__id__ = MathOp.__id__

    def calculate(self):
        pass

    def backward(self, edge_value):
        pass



