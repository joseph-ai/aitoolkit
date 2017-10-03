import networkx as nx


class CalcFlow(object):

    def __init__(self, value):

        self.value = value

        self.network = nx.DiGraph()

        self.last_node = None

    def _add_edge_binary(self, other, func):

        self._add_edge_unary(func)

        other.add_edge(func)

    def _add_edge_unary(self, func):

        if self.last_node is None:
            self.last_node = self

        self.network.add_edge(self.last_node, func, val=str(self.value))

        self.last_node = func

    def add_edge(self, func):

        self._add_edge_unary(func)

    def _compose(self, other):

        return nx.compose(self.network, other.network)

