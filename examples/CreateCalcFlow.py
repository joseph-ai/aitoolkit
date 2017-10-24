from toolkit.autodiff.scalar.FloatRv import FloatRv
from toolkit.autodiff.math import MathRv, IdentityRv


def test(x, y):

    return (x + y) * (x * y)


def test_add(x, y):

    return x+y


def backwards(result):

    toposort = result.topological_sort(reverse=True, predicate=lambda x: isinstance(x, MathRv))

    network = result.network

    identities = []
    for math_node in toposort:

        edges_proceeding_node = network.out_edges(math_node)

        # this is a leaf node and we set the seed to 1
        if len(edges_proceeding_node) == 0:
            math_node.result.partial_value = 1
            continue

        if isinstance(math_node, IdentityRv):
            identities.append(math_node)

        # update partials until you get to the root nodes
        for current_edge in edges_proceeding_node:

            for proceeding_node in current_edge:

                if math_node == proceeding_node:
                    continue

                edge_val = math_node.result

                proceeding_node_partial_wrt_edge_val = proceeding_node.backwards(edge_val)

                proceeding_node_partial_val = proceeding_node.result.partial_value

                math_node_partial_val = math_node.result.partial_value

                math_node_partial_val = math_node_partial_val \
                    + (proceeding_node_partial_val * proceeding_node_partial_wrt_edge_val)

                math_node.result.partial_value = math_node_partial_val

    return {node: node.result.partial_value for node in identities}


def simple_test():

    x = FloatRv.create(3.0)
    y = FloatRv.create(4.0)
    z = FloatRv.create(5.0)
    a = FloatRv.create(7.0)
    b = FloatRv.create(8.0)
    c = FloatRv.create(2.0)

    z3 = (((x+y) + (x+z) + (y+a)) * (b ** c)) * x

    return z3


def test_func(x1, x2):

    return (x1.ln() + (x1 * x2)) - x2.sin()


if __name__ == "__main__":

    v1 = FloatRv.create(2.0)
    v2 = FloatRv.create(5.0)
    z4 = test_func(v1, v2)
    zz = backwards(z4)




