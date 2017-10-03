import networkx as nx
from toolkit.autograd.scalar.FloatRv import FloatRv


def test(x, y):

    return (x + y) * (x * y)


def test_add(x, y):

    return x+y


if __name__ == "__main__":

    x = FloatRv.create(3.0)
    y = FloatRv.create(4.0)

    v = test_add(x, y)

    #print(v)




