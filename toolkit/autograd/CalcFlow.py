import networkx as nx


class CalcFlow(object):

    def __init__(self, value):

        self.value = value

        self.network = nx.DiGraph()

        self.last_node = None

    def _add_edge_to_both(self, other, func):

        self.add_edge(func)

        other.add_edge(func)

    def _add_edge_to_self(self, func):

        if self.last_node is None:
            self.last_node = self

        self.network.add_edge(self.last_node, func, val=str(self.value))

    def add_edge(self, func):

        self._add_edge_to_self(func)

    def _compose(self, other):
        network = nx.compose(self.network, other.network)
        return network

    def draw(self):

        import networkx as nx
        n = self.network
        pos = nx.spring_layout(n)
        nx.draw_networkx(n, pos)
        nx.draw_networkx_edge_labels(n, pos)

    def to_graphml(self):

        nx.write_graphml(self.network, "%s.xml" % str(self.value))
