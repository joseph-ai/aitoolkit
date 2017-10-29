from .flow import FlowCreator
from .math import MathOp, IdentityOp


class CalcFlow(object):

    def __init__(self, value):

        self.value = value

        self.gradient = 0.

        self.identity = None

        self.last_node = None

        self.flow = FlowCreator.default_creator()
        self.flow.init()

    def __calc_unary__(self, calc_val, func):

        self._add_edge_to_self(func)

        calc_val.last_node = func

        calc_val.flow = self.flow

        func.result = calc_val

        func.flow = calc_val.flow

        return calc_val

    def __calc_binary__(self, calc_val, other, func):

        self._add_edge_to_both(other, func)

        calc_val.flow = self.__compose__(other)

        calc_val.last_node = func

        func.result = calc_val

        func.flow = calc_val.flow

        return calc_val

    def _add_edge_to_both(self, other, func):

        self.add_edge(func)

        other.add_edge(func)

    def _add_edge_to_self(self, func):

        if self.last_node is None:
            self.last_node = self

        self.flow.add_edge(self.last_node, func, val=str(self))

        if self.identity is not None and self.last_node != self.identity:
            self.flow.add_edge(self.identity, func, val=str(self))

    def add_edge(self, func):

        self._add_edge_to_self(func)

    def __compose__(self, other):

        flow = self.flow.compose(other.flow)

        return flow

    def topological_sort(self, predicate=None, func=None):

        data = self.flow.topological_sort()

        predicate_data = data
        if predicate is not None:
            predicate_data = [x for x in data if predicate(x)]

        predicate_filter_data = predicate_data
        if func is not None:
            predicate_filter_data = [func(x) for x in predicate_data]

        return predicate_filter_data

    def backward(self):

        topological_sort = self.topological_sort(predicate=lambda x: isinstance(x, MathOp))

        identities = []
        for math_node in topological_sort:

            edges_proceeding_node = self.flow.out_edges(math_node)

            # this is a leaf node and we set the seed to 1
            if len(edges_proceeding_node) == 0:
                math_node.result.gradient = 1
                continue

            if isinstance(math_node, IdentityOp):
                identities.append(math_node)

            # update partials until you get to the root nodes
            for current_edge in edges_proceeding_node:

                for proceeding_node in current_edge:

                    if math_node == proceeding_node:
                        continue

                    edge_val = math_node.result

                    proceeding_node_partial_wrt_edge_val = proceeding_node.backward(edge_val)

                    proceeding_node_partial_val = proceeding_node.result.gradient

                    math_node_partial_val = math_node.result.gradient

                    math_node_partial_val = math_node_partial_val \
                        + (proceeding_node_partial_val * proceeding_node_partial_wrt_edge_val)

                    math_node.result.gradient = math_node_partial_val

        return {node.result: node.result.gradient for node in identities}

    @classmethod
    def is_calc_flow(cls, obj):
        return isinstance(obj, CalcFlow)


