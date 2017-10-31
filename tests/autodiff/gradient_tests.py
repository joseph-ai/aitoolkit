import unittest
import toolkit.autodiff.CalcFlow as c


from toolkit.autodiff.scalar.FloatScalar import FloatScalar
from toolkit import Session


class GradientTest(unittest.TestCase):

    def test_increment_id(self):

        sess = Session("test", True)
        with sess as s:
            v = FloatScalar.create(1.0)
            v1 = FloatScalar.create(3.33)
            self.assertEqual(v1.__id__, 4)

    def test_value_creation(self):

        sess = Session("test")
        with sess as s:
            v = FloatScalar.create(1.9)
            self.assertEqual(v.value, 1.9)

    def test_reset(self):

        sess = Session("test")
        with sess as s:
            v = FloatScalar.create(2.0)

        self.assertEqual(c.CalcFlow.__id__, 0)


if __name__ == "__main__":
    unittest.main()
