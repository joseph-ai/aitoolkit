import numpy as np

from toolkit.autodiff.scalar.FloatScalar import FloatScalar
from toolkit.autodiff.tensor.FloatTensor import FloatTensor


def test_func(x1, x2):

    return (x1.ln() + (x1 * x2)) - x2.sin()


if __name__ == "__main__":

    v1 = FloatScalar.create(2.0)
    v2 = FloatScalar.create(5.0)
    v3 = test_func(v1, v2)
    ans = v3.backward()
    print("\nv1.gradient: %s\nv2.gradient: %s" % (v1.gradient, v2.gradient))

    t1 = FloatTensor.create(np.array([2.0]))
    t2 = FloatTensor.create(np.array([5.0]))
    t3 = test_func(t1, t2)
    tb = t3.backward()
    print("\nt1.gradient: %s\nt2.gradient: %s" % (t1.gradient, t2.gradient))




