def trace(fn):
    def inner(x):
        y = fn(x)
        print "Calling {0} and it returns {1}".format(fn.__name__, y)
        return y
    return inner


def square(x):
    return x*x


@trace
def square2(x):
    return square(x)

n = square2(7)
