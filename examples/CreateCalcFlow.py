from toolkit.autodiff.scalar.FloatRv import FloatRv
from toolkit.autodiff.math import MathRv


def test(x, y):

    return (x + y) * (x * y)


def test_add(x, y):

    return x+y


if __name__ == "__main__":

    x = FloatRv.create(3.0)
    y = FloatRv.create(4.0)
    z = FloatRv.create(5.0)
    a = FloatRv.create(7.0)
    b = FloatRv.create(8.0)
    c = FloatRv.create(2.0)

    z3 = (((x+y) + (x+z) + (y+a)) * (b ** c)) / x

    is_mathrv = lambda node: isinstance(node, MathRv)

    z3_sortedGraph = z3.topological_sort(reverse=True, predicate=is_mathrv)


