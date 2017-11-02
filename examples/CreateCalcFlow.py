import numpy as np

from toolkit.autodiff.scalar.FloatScalar import FloatScalar
from toolkit.autodiff.tensor.FloatTensor import FloatTensor
from toolkit import Session


def test_func(x1, x2):

    return (x1.ln() + (x1 * x2)) - x2.sin()


if __name__ == "__main__":

    session = Session("MySession")

    with session as s:
        v1 = FloatScalar.create(2.0)
        v2 = FloatScalar.create(5.0)
        v3 = test_func(v1, v2)
        ans = v3.backward()
        print("\nv1.gradient: %s\nv2.gradient: %s" % (v1.gradient, v2.gradient))

    with session as s:
        v11 = FloatScalar.create(4.0)
        v21 = FloatScalar.create(10.0)
        v31 = test_func(v11, v21)
        ans = v31.backward()
        print("\nv11.gradient: %s\nv21.gradient: %s" % (v11.gradient, v21.gradient))

    with session as s:
        t1 = FloatTensor.create(np.array([2.0]))
        t2 = FloatTensor.create(np.array([5.0]))
        t3 = test_func(t1, t2)
        tb = t3.backward()
        print("\nt1.gradient: %s\nt2.gradient: %s" % (t1.gradient, t2.gradient))

    with session as s:
        m1 = FloatTensor.create(np.array([2.0, 4.0]))
        m2 = FloatTensor.create(np.array([5.0, 10.0]))
        m3 = test_func(m1, m2)
        mb = m3.backward()
        print("\nm1.gradient: %s\nm2.gradient: %s" % (m1.gradient, m2.gradient))


