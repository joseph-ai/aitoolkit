import networkx as nx


class CalcFlow(object):

    def __init__(self, value):

        self.value = value

        self.partial_value = 0

        self.network = nx.DiGraph()

        self.identity = None
        self.last_node = None

    def _add_edge_to_both(self, other, func):

        self.add_edge(func)

        other.add_edge(func)

    def _add_edge_to_self(self, func):

        if self.last_node is None:
            self.last_node = self

        self.network.add_edge(self.last_node, func, val=str(self))

        if self.identity is not None:
            self.network.add_edge(self.identity, func, val=str(self))

    def add_edge(self, func):

        self._add_edge_to_self(func)

    def _compose(self, other):

        network = nx.compose(self.network, other.network)

        return network

    def topological_sort(self, reverse=False, predicate=None, func=None):

        data = nx.topological_sort(self.network, reverse=reverse)

        predicate_data = data
        if predicate is not None:
            predicate_data = [x for x in data if predicate(x)]

        predicate_filter_data = predicate_data
        if func is not None:
            predicate_filter_data = [func(x) for x in predicate_data]

        return predicate_filter_data

    def leaves(self):

        network = self.network

        return [x for x in nx.nodes_iter(network)
                if network.out_degree(x) == 0
                and network.in_degree(x) != 0]

    def in_edges(self, leaves=None, data=False):

        network = self.network

        if leaves is None:
            leaves = self.leaves()

        in_edges = [x for x in network.in_edges(leaves, data)]

        return in_edges

    @classmethod
    def isCalcFlow(cls, obj):
        return isinstance(obj, CalcFlow)

    def draw(self):

        n = self.network
        pos = nx.spring_layout(n)
        nx.draw_networkx(n, pos)
        nx.draw_networkx_edge_labels(n, pos)

    def to_graphml(self, file_path="data.xml"):

        nx.write_graphml(self.network, file_path)
