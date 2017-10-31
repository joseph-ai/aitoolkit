import networkx as nx


class NxFlow(object):

    def __init__(self, *args, **kwargs):

        self.network = None

    def init(self):
        self.network = nx.DiGraph()

    def compose(self, other):

        n = NxFlow()
        n.network = nx.compose(self.network, other.network)

        return n

    def topological_sort(self):

        return nx.topological_sort(self.network, reverse=True)

    def leaves(self):

        network = self.network

        return [x for x in network.nodes_iter()
                if network.out_degree(x) == 0
                and network.in_degree(x) != 0]

    def add_edge(self, node1, node2, val):

        self.network.add_edge(node1, node2, val=val)

    def in_edges(self, leaves, data=False):

        return self.network.in_edges(leaves, data)

    def out_edges(self, node):

        return self.network.out_edges(node)

    def write(self, file_path="data.xml"):

        nx.write_graphml(self.network, file_path)

    def draw(self):

        n = self.network
        pos = nx.spring_layout(n)
        nx.draw_networkx(n, pos)
        nx.draw_networkx_edge_labels(n, pos)



