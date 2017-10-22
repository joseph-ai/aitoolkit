from toolkit.autodiff.scalar.FloatRv import FloatRv
from toolkit.autodiff.math import MathRv


def test(x, y):

    return (x + y) * (x * y)


def test_add(x, y):

    return x+y


def backwards(result):

    result.partial_value = 1

    toposort = result.topological_sort(reverse=True)

    network = result.network

    for item in toposort:

        out_edges = network.out_edges(item)

        if len(out_edges) == 0:
            print("Leaf Node => %s" % item)
            continue

        for edges in out_edges:
            for node in edges:
                if item != node:
                    print("Item:%s\nNode:%s" % (str(item), node))
                    edge_val = item.result
                    print("%s:%s" % (type(edge_val), edge_val))
                    partial = node.backwards(edge_val)
                    print("Edge:%s\nPartial:%s" % (edge_val, partial))
                    print("--")

    return result


def test_func(x1, x2):

    return (x1.ln() + (x1 * x2)) - x2.sin()


def simple_test():

    x = FloatRv.create(3.0)
    y = FloatRv.create(4.0)
    z = FloatRv.create(5.0)
    a = FloatRv.create(7.0)
    b = FloatRv.create(8.0)
    c = FloatRv.create(2.0)

    z3 = (((x+y) + (x+z) + (y+a)) * (b ** c)) * x

    return z3


if __name__ == "__main__":

    v1 = FloatRv.create(2.0)
    v2 = FloatRv.create(5.0)
    z4 = test_func(v1, v2)
    zz = backwards(z4)




