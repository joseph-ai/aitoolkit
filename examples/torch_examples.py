import numpy as np
import torch

from torch.autograd import Variable


def test_func(x1, x2):

    return (x1.log() + (x1 * x2)) - x2.sin()



def test_func_dot(x1, x2):

    return x1.dot(x2)


def test_func_mm(x1, x2):

    return torch.mm(x1, x2)


if __name__ == '__main__':

    n1 = np.array([[2., 4.], [9., 5.]])
    n2 = np.array([[5., 10.], [3., 2.]])

    t1 = Variable(torch.from_numpy(n1), requires_grad=True)
    t2 = Variable(torch.from_numpy(n2), requires_grad=True)

    #result = test_func(t1, t2)
    #result = test_func_dot(t1, t2)

    result = test_func_mm(t1, t2)

    result1 = result.sum()
    result1.backward()

    print("---t1---\nvalue\n%s\ngrad\n%s\n" % (t1, t1.grad))
    print("---t2---\nvalue\n%s\ngrad\n%s\n" % (t2, t2.grad))



