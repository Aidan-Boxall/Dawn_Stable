def average(x, y):
    return (x+y)/2.0
print average(5,6)
a = average
a.a=100
x = a(5,6)
print x