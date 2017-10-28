import toolkit.autodiff.scalar.FloatFw as ff


def func1(x, y, z):

    return (x * x) + (x * y) + (x * z)


# regular use of the function
print(func1(3.0, 4.0, 5.0))

x = ff.FloatFw(3.0, 1.0)
y = ff.FloatFw(4.0, 0.0)
z = ff.FloatFw(5.0, 0.0)

result = func1(x, y, z)

print(result.val)
print(result.delta)


