from toolkit.autodiff.scalar.FloatScalar import FloatScalar

def test(x, y):

    return (x + y) * (x * y)


def test_add(x, y):

    return x+y


def test_func(x1, x2):

    return (x1.ln() + (x1 * x2)) - x2.sin()


if __name__ == "__main__":

    v1 = FloatScalar.create(2.0)
    v2 = FloatScalar.create(5.0)
    z4 = test_func(v1, v2)
    zz = z4.backwards()
    print("\nForward: %s\nv1.gradient: %s\nv2.gradient: %s" % (z4, v1.gradient, v2.gradient))




