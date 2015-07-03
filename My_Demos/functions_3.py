def f(a, b, c=100):
    print a, b, b + (b-a)
f(60,30)


def g(x, **kwargs):
    try:
        print kwargs['mouse']
        if kwargs['mouse'] is not None:
            print 'yes'
    except:
        pass
    print x

g(5, mouse='dog')