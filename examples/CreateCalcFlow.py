from toolkit.autodiff.scalar.FloatRv import FloatRv
from toolkit.autodiff.math import MathRv


def test(x, y):

    return (x + y) * (x * y)


def test_add(x, y):

    return x+y


def backwards(result):

    toposort = result.topological_sort(reverse=True)

    network = result.network

    for item in toposort:

        out_edges = network.out_edges(item)

        if len(out_edges) == 0:
            print("Leaf Node => %s" % item)
            item.backwards(seed=1.0)
            continue

        for edges in out_edges:
            for node in edges:
                if item != node:
                    partial = node.backwards_result
                    item.backwards(value=partial)
                    print("%s -> %s" % (str(item), node))


if __name__ == "__main__":

    x = FloatRv.create(3.0)
    y = FloatRv.create(4.0)
    z = FloatRv.create(5.0)
    a = FloatRv.create(7.0)
    b = FloatRv.create(8.0)
    c = FloatRv.create(2.0)

    z3 = (((x+y) + (x+z) + (y+a)) * (b ** c)) * x

    backwards(z3)



